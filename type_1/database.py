from pathlib import Path

import pandas as pd

from type_1.tree import read_tree
from type_1.models import T1Database

import joblib


def build_database(dir: Path) -> T1Database:
    tree = read_tree(dir / Path("taxonomy.tree"))
    classifier = joblib.load(dir / Path("classifier.pkl"))
    db_features = pd.read_csv(dir / Path("db_features.csv"), index_col=0, header=0)
    return T1Database(
        path=dir,
        classifier=classifier,
        database_metadata=db_features,
        tree=tree
    )


def annotate_gtdb_features(df_metadata: pd.DataFrame, bacteria_metadata: Path, archaea_metadata: Path) -> pd.DataFrame:
    df_bac = pd.read_csv(bacteria_metadata, sep="\t")
    df_arch = pd.read_csv(archaea_metadata, sep="\t")

    df = pd.concat((df_arch, df_bac))

    df.columns = ["gf_" + col for col in df.columns]

    df['assembly_accession'] = [_.replace("GB_", "").replace("RS_", "") for _ in df['gf_accession']]

    df_merged = pd.merge(df_metadata, df, on="assembly_accession")
    return df_merged
