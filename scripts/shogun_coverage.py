#!/usr/bin/env python
from glob import glob
import os

# %%
base_path = "/project/flatiron2/ben/projects/type_1/data"

shogun_db = "/project/flatiron/data/shogun/rep202_ab"

b6_files = glob(f"{base_path}/mock_communities/**/filter/allpath.r202.b6", recursive=True)

# %%
for b6_file in b6_files:
    base_path = os.path.dirname(b6_file)

    command_coverage = f"""/usr/bin/time -v shogun coverage\
        --input {b6_file} \
        --database {shogun_db} \
        --level species \
        --taxonomy_mapping \
        -o {base_path}/coverage.r202.txt \
        > {base_path}/shogun.coverage.r202.log 2>&1"""
    print(command_coverage)

    command_taxonomy = f"""/usr/bin/time -v shogun assign_taxonomy\
        --input {b6_file} \
        --database {shogun_db} \
        --aligner burst
        --level species \
        --no-capitalist \
        -o {base_path}/shogun.taxonomy.r202.txt \
        > {base_path}/shogun.taxonomy.r202.log 2>&1"""
    print(command_taxonomy)

    command_capitalist = f"""/usr/bin/time -v shogun assign_taxonomy\
        --input {b6_file} \
        --database {shogun_db} \
        --aligner burst
        --level species \
        -o {base_path}/shogun.capitalist.r202.txt \
        > {base_path}/shogun.capitalist.r202.log 2>&1"""
    print(command_capitalist)
