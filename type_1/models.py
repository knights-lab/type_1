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
    # TODO: This value should always be between 0 and 1
    percent_coverage: float
    # TODO: This value should always be greater than 0
    mean_coverage: float
    # TODO: Make sure this is not undefined
    sd_coverage: float
    # TODO: This value should always be between 0 and 1
    percent_padded_coverage: float
    # TODO: This value should always be greater than 0
    mean_padded_coverage: float
    # TODO: This value should always be between 0 and 1
    expected_percent_coverage: float
    # TODO: This value should always be defined
    shannon_entropy: float
    # TODO: This value should always be between 0 and 1 (sometimes it is two)
    percent_max_uncovered_region: float
    # TODO: Should always be an integer greater than 0
    largest_pileup: int
