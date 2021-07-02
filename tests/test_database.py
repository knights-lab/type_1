from pathlib import Path
import pytest
from typing import Union

import os

from type_1.main import filter_alignment
from type_1.models import T1Database
from type_1.database import build_database


@pytest.fixture
def gtdb_test_database() -> Path:
    return os.path.join("fixtures", "database")


@pytest.fixture()
def test_b6() -> Path:
    return Path("fixtures") / Path("test.sort.1k.b6")


def test_pipeline(gtdb_test_database, test_b6, tmp_path):
    df_results = filter_alignment(gtdb_test_database, test_b6, tmp_path)
    print(df_results)
