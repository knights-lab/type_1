from pathlib import Path


import pytest

from type_1.main import features_alignment


@pytest.fixture
def alignment_allpath() -> Path:
    return Path("fixtures") / Path("allpath.r202.head.b6")

@pytest.fixture
def alignment_allpath_coverage() -> Path:
    return Path("fixtures") / Path("allpath.coverage.ungapped.b6")


@pytest.fixture()
def database_features() -> Path:
    return Path("fixtures") / Path("db_features.csv")


def test_alignment_length(alignment_allpath, database_features, tmp_path):
    outf = tmp_path / Path("features.txt")
    features_alignment(database_features=database_features, alignment=alignment_allpath, outf=outf)


def test_alignment_coverage(alignment_allpath_coverage, database_features, tmp_path):
    outf = tmp_path / Path("features.txt")
    features_alignment(database_features=database_features, alignment=alignment_allpath_coverage, outf=outf)
