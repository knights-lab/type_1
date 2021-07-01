import os
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
