import pathlib
import pytest
from typing import Union

import os

from type_1.models import T1Database
from type_1.database import build_database


@pytest.fixture
def gtdb_test_database() -> T1Database:
    return build_database(os.path.join("fixtures", "database"))


def test_check_database(gtdb_test_database):
    print(gtdb_test_database.tree)

