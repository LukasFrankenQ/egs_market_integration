<!--
SPDX-FileCopyrightText: 2017-2023 The PyPSA-Eur Authors
SPDX-License-Identifier: CC-BY-4.0
-->

### Code and Data for: Market Integration Pathways for Enhanced Geothermal Systems in Europe

This repo provides supplementary data for the paper: [insert link].

#### How to use

The figures from the are generated by the notebooks and the data is also provided here. To run these, 

1. install `envs/envoronment.yaml` and your local machine and activate it.
2. unzip the zip-directory `plotting_data`.
3. modify `notebooks/data_path.py` to point into the first layer of the unzipped directory.
4. run the notebooks.

If you wish to re-run some of modelling

1. install `envs/envoronment.yaml` and your local machine and activate it.
2. check inside `plotting_data` which wildcards have been used for the model.
4. (refer to `https://pypsa-eur.readthedocs.io/en/latest` for documentation on running the model.)
3. execute the model with the respective wildcards.
