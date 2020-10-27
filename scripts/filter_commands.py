#!/usr/bin/env python
from glob import glob
import os

# %%
base_path = "/project/flatiron2/ben/projects/type_1/data"

shogun_database = "/project/flatiron/data/shogun/rep202_ab"

query_files = glob(f"{base_path}/mock_communities/**/combined_seqs.fna", recursive=True)

# %%
for query_file in query_files:
    base_query_path = os.path.dirname(query_file)

    burst_command = f"""/usr/bin/time -v shogun \
  filter \
  -i {query_file} \
  -d {shogun_database} \
  -o {base_query_path}/filter \
  > {base_query_path}/allpath.r202.filter.log 2>&1
"""
    print(burst_command)
