#!/usr/bin/env python
from glob import glob
import os
import re

# %%
base_path = "/project/flatiron2/ben/projects/type_1/data"

query_files = glob(f"{base_path}/mock_communities/**/filter/allpath.r202.b6", recursive=True)

# %%
for query_file in query_files:
    base_query_path = os.path.dirname(query_file)
    result = re.search(r"/mock_communities/(.*)/filter/allpath.r202.b6", query_file)
    group_1 = result.group(1)
    rsync_command = f"""mkdir ./mock_communities/{group_1}/filter && rsync -rP hillm096@teraminx.cs.umn.edu:{base_query_path}/allpath.r202.b6 ./mock_communities/{group_1}/filter/allpath.r202.b6"""
    print(rsync_command)


