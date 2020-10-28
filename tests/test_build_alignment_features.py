import os
import pathlib
from typing import Union
from collections import Counter, defaultdict
import csv

import pytest
import numpy as np

from type_1.features import get_expected_coverage, zero_runs
from type_1.utils import read_fasta


@pytest.fixture
def alignment_allpath() -> Union[str, pathlib.Path]:
    return os.path.join("fixtures", "allpath.r202.head.b6")


def test_genome_length(alignment_allpath):
    pass
