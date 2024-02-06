# -*- coding: utf-8 -*-
# SPDX-FileCopyrightText: : 2023 @LukasFranken, The PyPSA-Eur Authors
#
# SPDX-License-Identifier: MIT
"""
This rule extracts potential and cost for electricity generation through
enhanced geothermal systems.

For this, we use data from "From hot rock to useful energy..." by Aghahosseini, Breyer (2020)
'https://www.sciencedirect.com/science/article/pii/S0306261920312551'
Note that we input data used here is not the same as in the paper, but was passed on by the authors.

The data provides a lon-lat gridded map of Europe (1° x 1°), with each grid cell assigned
a heat potential (in GWh) and a cost (in EUR/MW).

This scripts overlays that map with the network's regions, and builds a csv with CAPEX, OPEX and p_nom_max
"""

import logging

logger = logging.getLogger(__name__)

import json

import geopandas as gpd
import numpy as np
import pandas as pd
import xarray as xr
import warnings
from shapely.geometry import Polygon

warnings.filterwarnings("ignore")


def prepare_egs_data(egs_file):
    with open(egs_file) as f:
        jsondata = json.load(f)

    def point_to_square(p, lon_extent=1.0, lat_extent=1.0):
        try:
            x, y = p.coords.xy[0][0], p.coords.xy[1][0]
        except IndexError:
            return p

        return Polygon(
            [
                [x - lon_extent / 2, y - lat_extent / 2],
                [x - lon_extent / 2, y + lat_extent / 2],
                [x + lon_extent / 2, y + lat_extent / 2],
                [x + lon_extent / 2, y - lat_extent / 2],
            ]
        )

    years = [2015, 2020, 2025, 2030, 2035, 2040, 2045, 2050]
    lcoes = ["LCOE50", "LCOE100", "LCOE150"]

    egs_data = dict()

    for year in years:
        df = pd.DataFrame(columns=["Lon", "Lat", "CAPEX", "HeatSust", "PowerSust"])

        for lcoe in lcoes:
            for country_data in jsondata[lcoe]:
                try:
                    country_df = pd.DataFrame(
                        columns=df.columns,
                        index=range(len(country_data[0][years.index(year)]["Lon"])),
                    )
                except TypeError:
                    country_df = pd.DataFrame(columns=df.columns, index=range(0))

                for col in df.columns:
                    country_df[col] = country_data[0][years.index(year)][col]

                if country_df.dropna().empty:
                    continue
                elif df.empty:
                    df = country_df.dropna()
                else:
                    df = pd.concat((df, country_df.dropna()), ignore_index=True)

        gdf = gpd.GeoDataFrame(
            df.drop(columns=["Lon", "Lat"]), geometry=gpd.points_from_xy(df.Lon, df.Lat)
        ).reset_index(drop=True)

        gdf["geometry"] = gdf.geometry.apply(lambda geom: point_to_square(geom))
        egs_data[year] = gdf

    return egs_data


def get_capacity_factors(network_regions_file, air_temperatures_file):
    """
    Performance of EGS is higher for lower temperatures, due to more efficient
    air cooling Data from Ricks et al.: The Role of Flexible Geothermal Power
    in Decarbonized Elec Systems.
    """

    delta_T = [-15, -10, -5, 0, 5, 10, 15, 20]
    cf = [1.17, 1.13, 1.07, 1, 0.925, 0.84, 0.75, 0.65]

    x = np.linspace(-15, 20, 200)
    y = np.interp(x, delta_T, cf)

    upper_x = np.linspace(20, 25, 50)
    m_upper = (y[-1] - y[-2]) / (x[-1] - x[-2])
    upper_y = upper_x * m_upper - x[-1] * m_upper + y[-1]

    lower_x = np.linspace(-20, -15, 50)
    m_lower = (y[1] - y[0]) / (x[1] - x[0])
    lower_y = lower_x * m_lower - x[0] * m_lower + y[0]

    x = np.hstack((lower_x, x, upper_x))
    y = np.hstack((lower_y, y, upper_y))

    network_regions = gpd.read_file(network_regions_file).set_crs(epsg=4326)
    index = network_regions["name"]

    air_temp = xr.open_dataset(air_temperatures_file)

    snapshots = pd.date_range(freq="h", **snakemake.params.snapshots)
    capacity_factors = pd.DataFrame(index=snapshots)

    for bus in index:
        temp = air_temp.sel(name=bus).to_dataframe()["temperature"]
        capacity_factors[bus] = np.interp((temp - temp.mean()).values, x, y)

    return capacity_factors


def prepare_capex():

    prepared_data = prepare_egs_data(snakemake.input.egs_cost)
    
    """PREPROCESSING"""
    for key, item in prepared_data.items():
        prepared_data[key] = item.groupby("geometry").mean().reset_index()

    df = pd.DataFrame(columns=prepared_data.keys())
    for year in df.columns:

        year_data = prepared_data[year].groupby("geometry").mean().reset_index()

        for g in year_data.geometry:

            if not g in year_data.geometry.tolist():
                continue
            df.loc[g, year] = year_data.loc[year_data.geometry == g, "CAPEX"].values[0]


    X = list()
    y = list()

    for i, row in df.iloc[:,::-1].iterrows():
        row = row.loc[row.notna()]

        for j, value in enumerate(row.values):

            if j == len(row) - 1:
                break

            X.append([value, row.index[j]])
            y.append(row.values[j+1])

    X = np.array(X)
    y = np.array(y)

    factor_mean = pd.Series(index=np.unique(X[:,1]).astype(int)).sort_index()

    for year in factor_mean.index:

        mask = X[:,1] == year
        factor_mean.loc[year] = (y[mask] / X[mask, 0]).mean()

    """PROCESSING CAPEX"""

    capex = pd.DataFrame(index=prepared_data[2050].geometry, columns=prepared_data.keys())

    capex.loc[:, 2050] = prepared_data[2050]["CAPEX"]
    for sooner, later in zip(capex.columns[::-1][1:], capex.columns[::-1]):

        p = prepared_data[sooner]

        capex.loc[p.geometry, sooner] = p["CAPEX"]
        missing_idx = capex.loc[capex[sooner].isna()].index

        from_later = (
            capex[later]
            .loc[missing_idx]
        )

        capex.loc[missing_idx, [sooner]] = from_later * factor_mean.loc[later]

    # capacity_factor = 0.9
    print("params sector")
    print(snakemake.params.sector)

    orc_cost = 1900 # USD/kW; value from Aghahosseini, Breyer (2022)
    efficiency = snakemake.params.sector["egs_efficiency_electricity"]

    for year in capex.columns[1:]:

        orc_cost /= factor_mean.loc[year]
        capex.loc[:, year] = capex[year] - orc_cost

    # capex = capex / capacity_factor * efficiency
    capex *= efficiency
    
    print('At the end of get capex')
    print(capex.head())

    return capex



if __name__ == "__main__":
    if "snakemake" not in globals():
        from _helpers import mock_snakemake

        snakemake = mock_snakemake(
            "build_egs_potentials",
            simpl="",
            clusters=37,
        )
    
    capex = prepare_capex()

    regions = (
        gpd.read_file(snakemake.input.regions)
        .set_index("name")
        .set_crs("EPSG:4326")
    )

    capex_year = int(snakemake.wildcards["egs_capex"])
    assert capex_year in [2020, 2025, 2030, 2035, 2040, 2045, 2050]

    p = gpd.GeoDataFrame(
        capex[[capex_year]]
        .reset_index()
        .rename(columns={capex_year: "CAPEX"}), crs="EPSG:4326"
        )

    capexes_mean = list()
    capexes_min = list()

    for i, (region, row) in enumerate(regions.iterrows()):

        overlap = p.loc[p.geometry.intersects(row.geometry)]
        shares = (a := overlap.geometry.intersection(row.geometry).area) / a.sum()

        capexes_mean.append(shares.multiply(overlap["CAPEX"]).sum() or np.nan)
        capexes_min.append(overlap["CAPEX"].min() or np.nan)

    regions["capex_mean"] = capexes_mean
    regions["capex_min"] = capexes_min

    print(regions.head())

    (
        regions
        .reset_index()
        [["capex_mean", "capex_min", "name"]]
        .to_csv(snakemake.output["egs_costs"], index=False)
    )

    import sys
    sys.exit()


    sustainability_factor = 0.0025
    # the share of heat that is replenished from the earth's core.
    # we are not constraining ourselves to the sustainable share, but
    # inversely apply it to our underlying data, which refers to the
    # sustainable heat.

    config = snakemake.config

    egs_data = prepare_egs_data(snakemake.input.egs_cost)
    egs_cost_year = int(snakemake.wildcards["egs_capex"][4:])

    egs_data = egs_data[egs_cost_year]

    egs_data = egs_data.loc[egs_data["PowerSust"] > 0].reset_index(drop=True)
    egs_regions = egs_data.geometry

    network_regions = (
        gpd.read_file(snakemake.input.regions)
        .set_index("name", drop=True)
        .set_crs(epsg=4326)
    )

    overlap_matrix = pd.DataFrame(
        index=network_regions.index,
        columns=egs_data.index,
    )

    for name, polygon in network_regions.geometry.items():
        overlap_matrix.loc[name] = (
            egs_regions.intersection(polygon).area
        ) / egs_regions.area

    overlap_matrix.to_csv(snakemake.output["egs_overlap"])

    # consider not only replenished heat
    egs_data["p_nom_max"] = egs_data["PowerSust"] / sustainability_factor

    egs_data[["p_nom_max", "CAPEX"]].to_csv(snakemake.output["egs_potentials"])

    capacity_factors = get_capacity_factors(
        snakemake.input["regions"],
        snakemake.input["air_temperature"],
    )

    capacity_factors.to_csv(snakemake.output["egs_capacity_factors"])
