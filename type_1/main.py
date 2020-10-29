from pathlib import Path

import pandas as pd
import typer

from type_1.features import gen_blast_features, gen_fasta_features

app = typer.Typer()


@app.command()
def database_fasta(fasta: Path, outf: Path):
    df = pd.DataFrame((model.dict() for model in gen_fasta_features(fasta)))
    df.to_csv(outf)


@app.command()
def features_alignment(database_features: Path, alignment: Path,  outf: Path) -> None:
    df_database_features = pd.read_csv(
        database_features,
        index_col=0
    )

    df = pd.DataFrame(
        (model.dict() for model in gen_blast_features(df_database_features=df_database_features, alignment_allpath=alignment))
    )

    df_merged = pd.merge(df, df_database_features, on="assembly_accession", how="left")

    df_merged.to_csv(outf)


if __name__ == "__main__":
    app()
