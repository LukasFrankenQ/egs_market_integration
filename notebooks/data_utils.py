import os
import sys
import json
import pandas as pd
import geopandas as gpd
from shapely.geometry import Polygon

from pathlib import Path
from shapely.ops import unary_union

sys.path.append(str(Path.cwd()))

from plotting_constants import coarse_regions, reverse_coarse_regions


idx = pd.IndexSlice

regions = gpd.read_file(
    Path.cwd().parent.parent.parent /
    "cluster_data" /
    "old_data" /
    "resources" /
    "regions_onshore_elec_s_72.geojson"
    ).set_crs("EPSG:4326").set_index("name")


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


def prepare_data_for_plot(costs, region, year, sustainability_factor=0.0025):

    eta = 0.12

    if not region == "all":
        buses = coarse_regions[region]
    else:
        buses = list(reverse_coarse_regions)

    shape = gpd.GeoSeries([
        unary_union(
            regions.loc[buses].geometry
            ).buffer(0.01)
        ])

    inters = (p := costs[int(year)]).loc[p.geometry.intersects(shape.geometry[0])]
    inters.loc[:,["area"]] = inters.geometry.intersection(shape.geometry[0]).area

    inters.loc[:,["HeatSust"]] = inters["HeatSust"].mul(inters["area"])
    inters.loc[:,["PowerSust"]] = inters["PowerSust"].mul(inters["area"])

    inters.loc[:,["Power"]] = inters["PowerSust"] / sustainability_factor
    inters.loc[:,["HeatPower"]] = inters["Power"] / eta

    inters = inters.sort_values(by="CAPEX", ascending=True)
    inters.loc[:,["HeatSust_cumsum"]] = inters["HeatSust"].cumsum()
    inters.loc[:,["Power_cumsum"]] = inters["Power"].cumsum()
    inters.loc[:,["HeatPower_cumsum"]] = inters["HeatPower"].cumsum()
    
    return inters


root = Path.cwd().parent.parent.parent / "cluster_data"

def get_capacity_data(mode, op):

    index_col = [0,1,2]
    header = [0,1,2,3,4,5,6,7,8]

    """
    if mode == "chp" or mode == "dh":
        df = pd.read_csv(
            root / f"{mode}_data" / 
            # f"csvs_{op}" / 
            "nodal_capacities.csv", 
            index_col=index_col,
            header=header,
            )

    elif mode == "elec":
        if op == "flex":
            df = pd.read_csv(
                root / f"elec_data_flex" / "nodal_capacities.csv",
                index_col=index_col,
                header=header,
            )
        else:
            df = pd.read_csv(
                root / f"{mode}_data" / "nodal_capacities.csv",
                index_col=index_col,
                header=header,
            )
    """

    df = pd.read_csv(
        root /
        "breyer_sweep" /
        "joint_data" /
        "nodal_capacities.csv", 
        index_col=index_col, 
        header=header,
        )

    df = df.loc[:,idx[:,:,:,:,:,mode]].iloc[:,2:]
    
    df.columns = df.columns.droplevel([0,1,2,3,5,7,8])
    df = df.loc[idx[:,:,"injection geothermal heat"], idx[:,op]]
    df.columns = df.columns.droplevel([1])
    df.index = df.index.droplevel([0,2])

    return df.mul(1e-3)


def adjust_lightness(color, amount=0.5):
    import matplotlib.colors as mc
    import colorsys
    try:
        c = mc.cnames[color]
    except:
        c = color
    c = colorsys.rgb_to_hls(*mc.to_rgb(c))
    return colorsys.hls_to_rgb(c[0], max(0, min(1, amount * c[1])), c[2])