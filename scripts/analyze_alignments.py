#!/usr/bin/env ipython

#%%
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import warnings
import seaborn as sns

sns.set_style("darkgrid")
np.random.seed(930525)
pd.set_option('display.max_columns', 20)
pd.set_option('display.max_rows', 300)
warnings.simplefilter('once')

#%%
path_r201 = "/mnt/nvidia/pkr/code/type_1/data/mock_communities/zymo/ERR2935805/allpath.r201.b6"
# path_r92 = "/mnt/nvidia/pkr/code/type_1/data/mock_communities/zymo/ERR2935805/allpath.b6"


rows = []
with open(path_r201) as inf:
    for ix, line in enumerate(inf):
        row = line.split()
        rows.append([row[0], float(row[2])])
        if ix == 100:
            break

df_r201 = pd.DataFrame(rows, columns=["query", "score"])

rows = []
with open(path_r201) as inf:
    for ix, line in enumerate(inf):
        row = line.split()
        rows.append([row[0], float(row[2])])
        if ix == 100:
            break

# d_r92 = {}
# with open(path_r201) as inf:
#     for line in inf:
#         print(line)
#         row = line.split()
#         d_r92[row[0]] = float(row[2])

# query_name, reference, score
# ERR2935805.R2_13059762	GCF_003719725.1	100.000000	70	0	0	1	70	371996	372066	0	0




#%%

def main():
    pass


if __name__ == "main":
    main()

