from pathlib import Path

import pytest

from type_1.main import features_alignment
from type_1.models import AlignmentFeatures


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


def test_undefined_shannon_entropy():
    with pytest.raises(ValueError):
        AlignmentFeatures(
            assembly_accession="0",
            hits=1,
            percent_coverage=1,
            mean_coverage=1,
            sd_coverage=1,
            percent_padded_coverage=1,
            mean_padded_coverage=1,
            expected_percent_coverage=1,
            shannon_entropy=float('nan'),
            percent_max_uncovered_region=1,
            largest_pileup=1
        )


def test_coverage_greater_than_one():
    with pytest.raises(ValueError):
        AlignmentFeatures(
            assembly_accession="0",
            hits=1,
            percent_coverage=1,
            mean_coverage=1,
            sd_coverage=1,
            percent_padded_coverage=2,
            mean_padded_coverage=1,
            expected_percent_coverage=1,
            shannon_entropy=1,
            percent_max_uncovered_region=1,
            largest_pileup=1
        )
