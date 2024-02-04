import os
from pathlib import Path
from itertools import product
import time

sleep_length = 1200

# print("beginning with a sleep!")
# time.sleep(600)

root = "/exports/csce/eddie/eng/groups/energy-systems-group/projects/basic_egs/pypsa-eur/runs/run_data/"

template = "qsub -N {} -l h_vmem=64G -l h_rt=47:59:59 {} {}"

paths = [
    "chp_flex_72/run_1100_2050_0.3_True/",
    "chp_static_72/run_1100_2050_0.3_True/",
    "chp_flex_72/run_1200_2050_0.3_True/",
    "chp_static_72/run_1200_2050_0.3_True/",
    "chp_flex_72/run_1300_2050_0.3_True/",
    "chp_static_72/run_1300_2050_0.3_True/",
    "chp_flex_72/run_1400_2050_0.3_True/",
    "chp_static_72/run_1400_2050_0.3_True/",
    ]
names = [
    "CH1100F",
    "CH1100S",
    "CH1200F",
    "CH1200S",
    "CH1300F",
    "CH1300S",
    "CH1400F",
    "CH1400S",
    ]

non_nodes = ["node1f01", "node1f02", "node1j01", "node3c05", "node3c06"]

assert len(non_nodes) >= 2, "syntax breaks if there is not atleast two nodes"

non_nodes = "-l h=!" + " -l h=!".join(non_nodes)
tempfile = 'file.sh'

for path, name in zip(paths, names):

    print(f"Starting run {name}")

    mainfile = f"{root+path}main.sh"

    command = template.format(
        name,
        non_nodes,
        mainfile
        )

    f = open(tempfile, 'w')
    f.write(command)
    f.close()
    os.system(f'chmod +x {tempfile}')

    os.system('./'+tempfile)

    print(f"Starting sleep for {sleep_length} seconds.")
    time.sleep(sleep_length)
