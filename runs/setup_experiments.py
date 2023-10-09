import os
import yaml
import pandas as pd
from pathlib import Path
from itertools import product

import logging

logger = logging.getLogger(__name__)

capex_list = [1700]
# mode_list = ["elec", "dh", "chp"]
mode_list = ["chp"]
clusters = 72
egs_op = "flex"

security_lock = False

root = Path("/exports/csce/eddie/eng/groups/energy-systems-group/projects/basic_egs/pypsa-eur")


if security_lock:
	capex_list = capex_list[:1]
	mode_list = mode_list[:1]
	logger.warning("Security Lock is switched on, setting up only one experiment!")
else:
	logger.warning("Security Lock is switched off")

def retrieve_licence(lfile):
	lic = pd.read_csv(lfile, index_col=0)

	assert not lic.used.all(), "All Licences in licence storage are used up!"

	for i, row in lic.iterrows():
		if not row.used:
			current_lic = row.licences
			lic.loc[i, "used"] = True

			lic.to_csv(lfile)

			return current_lic


def setup_config(rundir, capex, mode, clusters, egs_op):

	config_base = root / "config" / "config.yaml"

	config_target = rundir / f"config_{int(capex)}_{mode}_{egs_op}.yaml"

	with open(config_base, "r") as f:
		config = yaml.safe_load(f)

	config["scenario"]["egs_capex"] = capex
	config["scenario"]["egs_mode"] = mode
	config["scenario"]["egs_op"] = egs_op
	config["scenario"]["clusters"] = clusters

	logger.info(f"Storing resulting config as {config_target}.")
	with open(config_target, "w") as f:
		yaml.dump(config, f)


def create_scripts(rundir, capex, mode, egs_op):

	main_fn = rundir / "main.sh"

	facil_fn = rundir / "facil.exp"
	get_licence_fn = rundir / "get_licence.sh"

	config_file = rundir / f"config_{int(capex)}_{mode}_{egs_op}.yaml"

	logger.info(f"Setting up main as {str(main_fn)}")

	model_template = "results/basic_test/{}networks/elec_s_{}_lv1.0__Co2L0-3H-T-H-B-I-solar+p3-dist1_2050_{}_{}_{}.nc"
	pre_model_name = model_template.format("pre", clusters, capex, mode, egs_op)
	post_model_name = model_template.format("post", clusters, capex, mode, egs_op)

	# main_fn = "testmain.sh"
	# facil_fn = "testfacil.exp"
	# get_licence_fn = "testlic.sh"

	try:
		os.remove(main_fn)
	except FileNotFoundError:
		pass

	try:
		os.remove(facil_fn)
	except FileNotFoundError:
		pass

	try:
		os.remove(get_licence_fn)
	except FileNotFoundError:
		pass

	##################################### MAIN SCRIPT ##########################################

	logger.info(f"Creating main file under {main_fn}.")
	f = open(main_fn, "w")

	f.write(". /etc/profile.d/modules.sh\n")
	f.write("module load anaconda/2022.05\n")

	f.write(f"chmod +x {str(rundir / 'facil.exp')}\n")
	f.write(f"chmod +x {str(rundir / 'get_licence.sh')}\n")

	f.write(f"expect {str(rundir / 'facil.exp')}\n")

	f.write(f"cd {str(root)}\n")

	f.write("snakemake --unlock\n")
	f.write("source activate basic-pypsa-eur\n")
	f.write(f"snakemake -call --touch --configfile {str(config_file)} -- {pre_model_name}\n")
	f.write(f"snakemake -call --configfile {str(config_file)} -- {pre_model_name}\n")

	f.write("snakemake --unlock\n")
	# f.write("source activate old-pypsa-eur\n")
	f.write(f"snakemake -call --touch --configfile {str(config_file)} -- {post_model_name}\n")
	f.write(f"snakemake -call --configfile {str(config_file)} -- {post_model_name}\n")

	f.close()
	os.system(f"chmod +x {main_fn}")

	##################################### EXPECT SCRIPT ########################################
    # (has the dialogue with the gurobi license retrieval)

	logger.info(f"Creating facil file under {facil_fn}.")
	f = open(facil_fn, "w")

	f.write(f"spawn {str(get_licence_fn)}\n")
	f.write('expect "hit Enter to store it in /home/s2216495"\n')
	f.write('send -- "\\r"\n')
	f.write('expect "Y/n"\n')
	f.write('send -- "y\\r"\n')
	f.write("expect eof\n")

	f.close()
	os.system(f"chmod +x {facil_fn}")

	##################################### GET LICENCE SCRIPT ###################################

	lic = retrieve_licence("licence_storage.csv")

	logger.info(f"Creating get licence file under {get_licence_fn}.")
	f = open(get_licence_fn, "w")

	f.write(f"/home/s2216495/opt/gurobi1000/linux64/bin/{lic}")

	f.close()
	os.system(f"chmod +x {get_licence_fn}")


for capex, mode in product(capex_list, mode_list):

	rundir = root / "runs" / "run_data" / f"{mode}_{egs_op}_{int(clusters)}" / f"run_{int(capex)}"
	print(f"Setting up experiment in dir {str(rundir)}")

	summary = f"CAPEX {capex}, mode {mode}, operation {egs_op}."
	try:

		if rundir.is_file():
			logger.warning(f"Rundir {str(rundir)} already exists.")
		os.makedirs(rundir, exist_ok=True)

		setup_config(rundir, capex, mode, clusters, egs_op)
		create_scripts(rundir, capex, mode, egs_op)

		print(f"Created run! {summary}")

	except:

		print(f"Failed to create run! {summary}.")
