import pandas as pd
from pydantic import BaseModel, validator
from pathlib import Path

from ete3 import Tree
from sklearn.base import BaseEstimator
import numpy as np


def between_zero_and_one(value: float) -> float:
    if 0 < value > 1:
        raise ValueError(f"Value {value} is not <= 0 and >= 1")
    return value


def greater_than_or_equal_to_zero(value: float) -> float:
    if value < 0:
        raise ValueError(f"Value {value} is not > 0.")
    return value


def is_finite(value: float) -> float:
    if not np.isfinite(value):
        raise ValueError(f"Value {value} is not finite")
    return value


class FastaFeatures(BaseModel):
    gc_content: float
    total_genome_length: int
    ungapped_genome_length: int
    num_n_groups: int
    consecutive_ns: int
    assembly_accession: str


class AlignmentFeatures(BaseModel):
    assembly_accession: str
    hits: int
    percent_coverage: float
    mean_coverage: float
    sd_coverage: float
    percent_padded_coverage: float
    mean_padded_coverage: float
    sd_padded_coverage: float
    percent_binned_coverage: float
    mean_binned_coverage: float
    sd_binned_coverage: float
    expected_percent_coverage: float
    shannon_entropy: float
    percent_max_uncovered_region: float
    largest_pileup: int
    largest_padded_pileup: int
    largest_binned_pileup: int

    _between_zero_and_one = validator(
        'percent_coverage',
        'percent_padded_coverage',
        'expected_percent_coverage',
        'percent_max_uncovered_region',
        'percent_binned_coverage', allow_reuse=True)(between_zero_and_one)
    _greater_than_or_equal_to_zero = validator(
        'mean_coverage',
        'mean_padded_coverage',
        'largest_pileup',
        'sd_padded_coverage',
        'mean_binned_coverage',
        'sd_binned_coverage',
        'largest_padded_pileup',
        'largest_binned_pileup', allow_reuse=True)(greater_than_or_equal_to_zero)
    _is_finite = validator('sd_coverage', 'shannon_entropy', allow_reuse=True)(is_finite)


class T1Database(BaseModel):
    path: Path
    tree: Tree
    classifier: BaseEstimator
    database_metadata: pd.DataFrame

    class Config:
        arbitrary_types_allowed = True

