from pathlib import Path
import pytest
from typing import Union

import pandas as pd

from type_1.main import filter_alignment
from type_1.features import gen_fasta_features
from type_1.database import annotate_gtdb_features


@pytest.fixture
def gtdb_test_database() -> Path:
    return Path("fixtures") / Path("database")


@pytest.fixture
def gtdb_20_fna() -> Union[str, Path]:
    return Path("fixtures") / Path("gtdb_20.fna")


@pytest.fixture()
def sorted_1k_b6() -> Path:
    return Path("fixtures") / Path("test.sort.1k.b6")


@pytest.fixture()
def gtdb_95_archaea_metadata() -> Path:
    return Path("fixtures") / Path("ar122_metadata_r95.filtered.tsv")


@pytest.fixture()
def gtdb_95_bacteria_metadata() -> Path:
    return Path("fixtures") / Path("bac120_metadata_r95.filtered.tsv")


# def test_pipeline(gtdb_test_database, sorted_1k_b6, tmp_path):
#     df_results = filter_alignment(gtdb_test_database, sorted_1k_b6, tmp_path)
#     print(df_results)


def test_annotate_gtdb_features(gtdb_20_fna: Path, gtdb_95_archaea_metadata: Path, gtdb_95_bacteria_metadata: Path):
    df = pd.DataFrame((model.dict() for model in gen_fasta_features(gtdb_20_fna)))
    df_results = annotate_gtdb_features(df, gtdb_95_archaea_metadata, gtdb_95_bacteria_metadata)
    assert df.shape[0] == df_results.shape[0]
