import pathlib
import pytest
from typing import Union

import os

from type_1.database import check_database


@pytest.fixture
def gtdb_test_database() -> Union[str, pathlib.Path]:
    return os.path.join("fixtures", "database")


def test_check_database(gtdb_test_database):
    check_database(gtdb_test_database)

