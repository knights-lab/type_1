from pathlib import Path
import os

import pandas as pd
import typer

from type_1.features import gen_blast_features, gen_fasta_features, get_tree_based_features

app = typer.Typer()


@app.command()
def database_fasta(fasta: Path, outf: Path) -> pd.DataFrame:
    df = pd.DataFrame((model.dict() for model in gen_fasta_features(fasta)))
    df.to_csv(outf)
    return df


@app.command()
def features_alignment(
    database_features: Path, alignment: Path,
    outf: Path, newick_tree: Path = None,
    num_bins: int = 10_000
) -> pd.DataFrame:
    df_database_features = pd.read_csv(
        database_features,
        index_col=0
    )

    df = pd.DataFrame(
        (model.dict() for model in gen_blast_features(
            df_database_features=df_database_features,
            alignment_allpath=alignment,
            num_bins=num_bins))
    )

    df_merged = pd.merge(df, df_database_features, on="assembly_accession", how="left")

    if newick_tree and os.path.exists(newick_tree):
        df_merged = get_tree_based_features(df_merged, newick_tree)

    df_merged.to_csv(outf)
    return df_merged


@app.command()
def features_tree(df_features: Path, newick_tree: Path, outf: Path) -> pd.DataFrame:
    df_features = pd.read_csv(
        df_features,
        index_col=0
    )

    df_merged = get_tree_based_features(df_features, newick_tree)

    df_merged.to_csv(outf)
    return df_merged


@app.command()
def filter_alignment(database_folder: Path, output_folder: Path) -> pd.DataFrame:
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)


if __name__ == "__main__":
    app()
