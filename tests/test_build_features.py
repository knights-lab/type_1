import os
import pathlib
from typing import Union
from collections import Counter

import pytest
import numpy as np

from type_1.features import genome_length, nucleotide_frequency, longest_consecutive_ns
from type_1.utils import read_fasta


@pytest.fixture
def gtdb_20_database() -> Union[str, pathlib.Path]:
    return os.path.join("fixtures", "gtdb_20.fna")


def test_genome_length(gtdb_20_database):
    d_genome_length = dict()
    with open(gtdb_20_database) as inf:
        for header, seq in read_fasta(inf):
            d_genome_length[header] = genome_length(seq)
    assert d_genome_length["GCA_000007185.1"] == 1_694_969
    assert d_genome_length["GCA_000007345.1"] == 5_751_492

    assert genome_length("ATCTATA") == 7


def test_nucleotide_frequency():
    freqs = nucleotide_frequency("ATATATC")

    assert freqs["N"] == 0
    assert freqs["A"] == 3
    assert freqs["T"] == 3
    assert freqs["C"] == 1


def test_longest_consecutive_ns(gtdb_20_database):
    d_genome_length = dict()
    with open(gtdb_20_database) as inf:
        for header, seq in read_fasta(inf):
            d_genome_length[header] = longest_consecutive_ns(seq)

    assert longest_consecutive_ns("ATTCNNN")[0] == 3
