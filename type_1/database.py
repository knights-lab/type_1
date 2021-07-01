import os
from pathlib import Path

from type_1.tree import read_tree
from type_1.models import T1Database


def build_database(dir: Path) -> T1Database:
    tree = read_tree(dir + Path("taxonomy.tree"))
