from pathlib import Path
import os
import pandas as pd
import typer

from type_1.database import build_database, annotate_gtdb_features
from type_1.features import gen_blast_features, gen_fasta_features, get_tree_based_features
from type_1.models import T1Database, CLASSIFIER_FEATURES

app = typer.Typer()


@app.command()
def database_fasta(fasta: Path, bacteria_metadata: Path, archaea_metadata: Path, outf: Path) -> pd.DataFrame:
    df = pd.DataFrame((model.dict() for model in gen_fasta_features(fasta)))

    df = annotate_gtdb_features(df, bacteria_metadata, archaea_metadata)

    df.to_csv(outf)
    return df


@app.command()
def features_alignment(
    database_dir: Path,
    alignment: Path,
    outf: Path,
    num_bins: int = 10_000
) -> pd.DataFrame:
    db = build_database(database_dir)
    df_merged = _get_features(db, alignment, num_bins=num_bins)
    df_merged.to_csv(outf)
    return df_merged


def _get_features(
    db: T1Database,
    alignment: Path,
    num_bins: int = 10_000
) -> pd.DataFrame:
    df = pd.DataFrame(
        (model.dict() for model in gen_blast_features(
            df_database_features=db.database_metadata,
            alignment_allpath=alignment,
            num_bins=num_bins))
    )

    df_merged = pd.merge(df, db.database_metadata, on="assembly_accession", how="left")

    df_merged = get_tree_based_features(df_merged, db.tree)

    return df_merged


@app.command()
def features_tree(database_path: Path, df_features: Path, outf: Path) -> pd.DataFrame:
    db = build_database(database_path)
    df_features = pd.read_csv(
        df_features,
        index_col=0
    )

    df_merged = get_tree_based_features(df_features, db.tree)

    df_merged.to_csv(outf)
    return df_merged


@app.command()
def filter_alignment(database_path: Path, alignment: Path, output_folder: Path, num_bins: int = 10_000) -> pd.DataFrame:
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    db = build_database(database_path)
    df_merged = _get_features(db, alignment, num_bins=num_bins)

    df_merged['relative_abundance'] = df_merged['hits'] / df_merged['hits'].sum()

    predictions = db.classifier.predict(df_merged[CLASSIFIER_FEATURES])

    prob_predictions = db.classifier.predict_proba(df_merged[CLASSIFIER_FEATURES])[:, 1]

    df_merged['predictions'] = predictions

    df_merged['predictions_proba'] = prob_predictions

    df_merged.to_csv(output_folder / Path("predictions.csv"))
    return df_merged


if __name__ == "__main__":
    app()
