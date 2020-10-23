import os
import pathlib
from typing import Union
from collections import Counter

import pytest
import numpy as np

# from type_1.features import length_of_genome
from type_1.utils import read_fasta


@pytest.fixture
def gtdb_20_database() -> Union[str, pathlib.Path]:
    return os.path.join("fixtures", "gtdb_20.fna")


def test_length_of_genome(gtdb_20_database):
    genome_length = dict()
    with open(gtdb_20_database) as inf:
        for header, seq in read_fasta(inf):
            genome_length[header] = len(seq)
            print(Counter(seq))
            print(seq.count("N"))

