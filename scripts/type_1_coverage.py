#!/usr/bin/env python
from glob import glob
import os

# %%
base_path = "/mnt/btrfs/data/type_1/species_mc"

db_features = "/mnt/nvidia/pkr/code/type_1/data/db_features.csv"

b6_files = glob(f"{base_path}/*/filter/allpath.r202.b6", recursive=True)

# %%
for b6_file in b6_files:
    base_path = os.path.dirname(b6_file)

    command_coverage = f"""/usr/bin/time -v python /mnt/nvidia/pkr/code/type_1/type_1/main.py features-alignment \
{db_features} \
{b6_file} \
{base_path}/t1.coverage.r202.txt \
> {base_path}/t1.coverage.t1.r202.log 2>&1"""
    print(command_coverage)
