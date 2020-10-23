from pathlib import Path
from typing import Generator

import pandas as pd
import typer

from type_1.utils import read_fasta
from type_1.features import genome_length, nucleotide_frequency, longest_consecutive_ns
from type_1.models import FastaFeatures

app = typer.Typer()


def gen_fasta_features(fasta: Path) -> Generator[FastaFeatures, None, None]:
    with open(fasta) as inf:
        for header, seq in read_fasta(inf):
            length = genome_length(seq)
            freqs = nucleotide_frequency(seq)
            ns, num_groups = longest_consecutive_ns(seq)

            length -= freqs["N"]
            gc_content = (freqs["G"] + freqs["C"]) / length

            results = FastaFeatures(
                genome_length=length,
                num_n_groups=num_groups,
                consecutive_ns=ns,
                gc_content=gc_content,
                assembly_accession=header
            )
            yield results


@app.command()
def database_fasta(fasta: Path, outf: Path):
    df = pd.DataFrame((model.dict() for model in gen_fasta_features(fasta)))
    df.to_csv(outf)


if __name__ == "__main__":
    app()
