from pydantic import BaseModel


class FastaFeatures(BaseModel):
    gc_content: float
    genome_length: int
    num_n_groups: int
    consecutive_ns: int
    assembly_accession: str
    unique_counts: int


class AlignmentFeatures(BaseModel):
    assembly_accession: str
    hits: int
    percent_coverage: float
    expected_coverage: float
    percent_padded_coverage: float
    shannon_entropy: float
    percent_max_uncovered_region: float
    largest_pileup: int
