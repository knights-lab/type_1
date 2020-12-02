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
from collections import Counter
df_taxa = pd.read_csv("./data/r95/r95.gtdb.tax", names=["accession_number", "taxa"], sep="\t")

taxa = Counter([';'.join(row.split(";")[:7]) for row in df_taxa["taxa"]])

for key, value in taxa.items():
    if value > 1:
        print(key, value)

#%%
def main():
    pass


if __name__ == "main":
    main()

