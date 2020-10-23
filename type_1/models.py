from pydantic import BaseModel


class FastaFeatures(BaseModel):
    gc_content: float
    genome_length: int
    num_n_groups: int
    consecutive_ns: int
    assembly_accession: str
