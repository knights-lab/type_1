#!/usr/bin/env python
from glob import glob
import os

# %%
base_path = "/scratch.global/ben/type_1/species_mc"

burst_base_directory = "/scratch.global/ben/gtdb/gtdb_s5000_d301"

query_files = glob(f"{base_path}/**/combined_seqs.fna", recursive=True)

# %%
for query_file in query_files:
    base_query_path = os.path.dirname(query_file)

    burst_command = f"""/usr/bin/time -v burst15 \
  -t 128 \
  -q {query_file} \
  -a {burst_base_directory}.acx \
  -r {burst_base_directory}.edx \
  -o {base_query_path}/allpath.gtdb95.b6 \
  -m ALLPATHS \
  -fr \
  -i 0.98 \
  --noprogress \
  > {base_query_path}/allpath.gtdb95.log 2>&1"""
    print(burst_command)
