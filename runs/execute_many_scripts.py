import os
from pathlib import Path
from itertools import product
import time

sleep_length = 300

message_template()
root = "/exports/csce/eddie/eng/groups/energy-systems-group/projects/basic_egs/pypsa-eur/runs/"

template = "qsub -N {} -l h_vmem=64G -l h_rt=47:59:59 -l h=!({}) ./main.sh"


path = "elec_static/"
name = "TEST"
nodes = [""]






