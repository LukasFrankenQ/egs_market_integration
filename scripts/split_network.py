"""
Splits the network into its components as a workout for scp's inability to handle large files.
"""

import logging

import pypsa
import yaml

from _helpers import (
    configure_logging,
    override_component_attrs,
)

if __name__ == "__main__":

    logger = logging.getLogger(__name__)

    if "snakemake" not in globals():
        from _helpers import mock_snakemake

        snakemake = mock_snakemake(
            "split_network",
        )

    configure_logging(snakemake)

    overrides = override_component_attrs(snakemake.input.overrides)
    n = pypsa.Network(snakemake.input.network, override_component_attrs=overrides)

    n.generators.to_csv(snakemake.output.generators)
    n.loads.to_csv(snakemake.output.loads)
    n.links.to_csv(snakemake.output.links)
    n.storage_units.to_csv(snakemake.output.storage_units)
    n.stores.to_csv(snakemake.output.stores)

    n.generators_t.p.to_csv(snakemake.output.generators_t_p)
    n.loads_t.p_set.to_csv(snakemake.output.loads_t_pset)

    n.links_t.p0.to_csv(snakemake.output.links_t_p0)
    n.links_t.p1.to_csv(snakemake.output.links_t_p1)
    n.links_t.p2.to_csv(snakemake.output.links_t_p2)

    n.storage_units_t.p.to_csv(snakemake.output.storage_units_t_p)
    n.stores_t.e.to_csv(snakemake.output.stores_t_e)

    n.buses.to_csv(snakemake.output.buses)

    with open(snakemake.output.config, "w") as f:
        yaml.dump(snakemake.config, f)


