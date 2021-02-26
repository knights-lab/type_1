from pathlib import Path

import numpy as np

import pytest

from type_1.main import features_alignment, features_tree
from type_1.features import get_binned_coverage, read_tree
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


@pytest.fixture()
def tree() -> Path:
    return Path("fixtures") / Path("r95.gtdb.tree")


@pytest.fixture()
def test_b6() -> Path:
    return Path("fixtures") / Path("test.sort.b6")


@pytest.fixture()
def gis_features() -> Path:
    return Path("fixtures") / Path("gis.20.b6.extra.csv")


def test_alignment_length(alignment_allpath, database_features, tmp_path):
    outf = tmp_path / Path("features.txt")
    df = features_alignment(database_features=database_features, alignment=alignment_allpath, outf=outf)


def test_alignment_coverage(alignment_allpath_coverage, database_features, tmp_path):
    outf = tmp_path / Path("features.txt")
    df = features_alignment(database_features=database_features, alignment=alignment_allpath_coverage, outf=outf)


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


def test_binned_coverage():
    genome_size = 10_041
    num_reads = 100
    num_bins = 10
    x = np.random.randint(0, genome_size, size=(num_reads,))

    hist = get_binned_coverage(x, genome_size, num_bins=num_bins)

    assert hist.shape[0] == num_bins


def test_tree_reading(tree):
    tree = read_tree(tree)


def test_alignment_coverage_tree(alignment_allpath, database_features, tree, tmp_path):
    outf = tmp_path / Path("features.txt")
    df = features_alignment(
        database_features=database_features,
        alignment=alignment_allpath,
        newick_tree=tree,
        outf=outf
    )


def test_alignment_full_tree(test_b6, database_features, tree, tmp_path):
    outf = tmp_path / Path("features.txt")
    df = features_alignment(
        database_features=database_features,
        alignment=test_b6,
        newick_tree=tree,
        outf=outf
    )


def test_gis_features(gis_features, tree, tmp_path):
    outf = tmp_path / Path("features.tree.txt")
    df = features_tree(
        df_features=gis_features,
        newick_tree=tree,
        outf=outf
    )
