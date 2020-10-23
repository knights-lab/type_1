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
import os

#%%
# base data directory
base_dir = "/home/bhillmann/petard/code/type_1/data"

# path to assembly summary
path_assembly_summary = os.path.join(base_dir, "rep202", "assembly_summary.txt")

# path to taxmap.tsv
path_taxmap = os.path.join(base_dir, "rep202", "taxmap.tsv")

# path to lingenome log
path_lingenome_log = os.path.join(base_dir, "rep202", "log.txt")

# path to output file
path_outf = os.path.join(base_dir, "rep202", "assembly_stats.csv")

#%%
df_assembly_summary = pd.read_csv(path_assembly_summary, skiprows=1, sep="\t")

cols = list(df_assembly_summary.columns)
cols[0] = "assembly_accession"
df_assembly_summary.columns = cols

df_taxmap = pd.read_csv(path_taxmap, sep="\t", names=["assembly_accession", "taxonomy"])

df_join = pd.merge(df_assembly_summary, df_taxmap, on="assembly_accession", how="inner")

#%%
# parsing the lingenome log
list_num_sequences = []
with open(path_lingenome_log) as inf:
    for line in inf:
        if line.startswith("Considering:"):
            # 'Considering: GCF_000005825.2.fna.gz [3 records]\n'
            row = line.split()
            # ['Considering:', 'GCF_000005825.2.fna.gz', '[3', 'records]']
            list_num_sequences.append([".".join(row[1].split(".")[:-2]), int(row[2][1:])])

df_number_sequences = pd.DataFrame(list_num_sequences, columns=["assembly_accession", "number_sequences"])

df_join = pd.merge(df_join, df_number_sequences, on="assembly_accession", how="inner")

#%%
# write to a file
df_join.to_csv(path_outf, index=False)
