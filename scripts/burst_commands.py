#!/usr/bin/env python
from glob import glob
import os

# %%
base_path = "/project/flatiron2/ben/projects/type_1/data"

burst_base_directory = "/project/flatiron/data/shogun/rep201_ab/burst/refseq_s3333_d301"

query_files = glob(f"{base_path}/mock_communities/**/combined_seqs.fna", recursive=True)

# %%
for query_file in query_files:
    base_query_path = os.path.dirname(query_file)

    burst_command = f"""/usr/bin/time -v burst15 \
  -t 72 \
  -q {query_file} \
  -a {burst_base_directory}.acx \
  -r {burst_base_directory}.edx \
  -o {base_query_path}/allpath.r201.b6 \
  -m ALLPATHS \
  -fr \
  -i 0.98 \
  --noprogress \
  > {base_query_path}/allpath.r201.log 2>&1
"""
    print(burst_command)
for query_file in query_files:
    base_query_path = os.path.dirname(query_file)

    burst_command = f"""/usr/bin/time -v burst15 \
  -t 72 \
  -q {query_file} \
  -a {burst_base_directory}.acx \
  -r {burst_base_directory}.edx \
  -o {base_query_path}/allpath.r201.b6 \
  -m ALLPATHS \
  -fr \
  -i 0.98 \
  --noprogress \
  > {base_query_path}/allpath.r201.log 2>&1
"""
    print(burst_command)