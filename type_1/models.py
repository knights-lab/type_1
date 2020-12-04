from pydantic import BaseModel


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
    expected_percent_coverage: float
    shannon_entropy: float
    percent_max_uncovered_region: float
    largest_pileup: int
