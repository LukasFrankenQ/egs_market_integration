"""
Takes data from Ricks et al. 2023 to compute hourly efficiency
gains or losses 
"""


import logging

logger = logging.getLogger(__name__)

import json

import geopandas as gpd
import numpy as np
import pandas as pd
import xarray as xr
from shapely.geometry import Polygon

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



if __name__ == "__main__":
    if "snakemake" not in globals():
        from _helpers import mock_snakemake

        snakemake = mock_snakemake(
            "build_egs_efficiencies",
            simpl="",
            clusters=37,
        )

    config = snakemake.config

    network_regions = (
        gpd.read_file(snakemake.input.regions)
        .set_index("name", drop=True)
        .set_crs(epsg=4326)
    )

    capacity_factors = get_capacity_factors(
        snakemake.input["regions"],
        snakemake.input["air_temperature"],
    )

    capacity_factors.to_csv(snakemake.output["egs_efficiencies"])
