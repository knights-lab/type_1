from pathlib import Path
from typing import Tuple, Generator
import csv
from collections import Counter, defaultdict
import re

import numpy as np
import pandas as pd

from type_1.utils import read_fasta
from type_1.models import AlignmentFeatures, FastaFeatures


def genome_length(seq: str) -> int:
    return len(seq)


def nucleotide_frequency(seq: str) -> Counter:
    return Counter(seq)


def longest_consecutive_ns(seq: str) -> Tuple[int, int]:
    long = 0
    num_groups = 0
    for r in re.finditer(r'(N)\1+', seq):
        group = r.group()
        if len(group) > long:
            long = len(group)
        num_groups += 1
    return long, num_groups


def zero_runs(a):
    # Stack Overflow:
    # https://stackoverflow.com/questions/24885092/finding-the-consecutive-zeros-in-a-numpy-array
    # Create an array that is 1 where a is 0, and pad each end with an extra 0.
    iszero = np.concatenate(([0], np.equal(a, 0).view(np.int8), [0]))
    absdiff = np.abs(np.diff(iszero))
    # Runs start and end where absdiff is 1.
    ranges = np.where(absdiff == 1)[0].reshape(-1, 2)
    return ranges


def get_expected_coverage(length_of_genome: int, number_of_trials: int) -> float:
    # https://math.stackexchange.com/questions/32800/probability-distribution-of-coverage-of-a-set-after-x-independently-randomly
    num = length_of_genome * (1 - np.power((length_of_genome - 1) / length_of_genome, number_of_trials))
    return num / length_of_genome


def gen_blast_features(
    alignment_allpath: Path,
    df_database_features: pd.DataFrame,
    padding: int = 100
) -> Generator[AlignmentFeatures, None, None]:
    d_reference_name_to_alignments = defaultdict(list)
    with open(alignment_allpath) as inf:
        inf_csv = csv.reader(inf, delimiter="\t")
        for row in inf_csv:
            # [
            #   'ERR2935805.R2_218359', read_name
            #   'GCF_000196035.1', reference_name
            #   '100.000000', alignment_score
            #   '65',
            #   '0',
            #   '0',
            #   '1',
            #   '65',
            #   '199883', alignment_start
            #   '199948', alignment_end
            #   '0',
            #   '3'
            # ]
            reference_name = row[1]
            alignment = sorted((int(row[8]) - 1, int(row[9]) - 1))
            d_reference_name_to_alignments[reference_name].append(alignment)

    for reference_name, alignments in d_reference_name_to_alignments.items():
        # get the reference length
        query = df_database_features.query(f"assembly_accession == '{reference_name}'")
        if query.shape[0] != 1:
            print(f"ERROR WITH QUERY {reference_name}")
            print(query)
            continue

        reference_name_length = query.genome_length.iloc[0]

        coverage = np.zeros(shape=reference_name_length, dtype=int)
        padded_coverage = np.zeros(shape=reference_name_length, dtype=int)
        for alignment in alignments:
            end = alignment[1]
            if end > reference_name_length:
                end = reference_name_length

            beginning = alignment[0]
            if beginning < 0:
                beginning = 0

            coverage[beginning:end] += 1

            padded_end = end + padding
            if padded_end > reference_name_length:
                padded_end = reference_name_length

            padded_beginning = end - padding
            if padded_beginning < 0:
                padded_beginning = 0

            padded_coverage[padded_beginning:padded_end] += 1

        num_zeros = (coverage == 0).sum()

        hits = len(alignments)
        percent_coverage = reference_name_length / (1-(num_zeros / reference_name_length))

        expected_coverage = get_expected_coverage(reference_name_length, np.sum(coverage))

        num_zeros_padded = (padded_coverage == 0).sum()
        percent_padded_coverage = reference_name_length / (1-(num_zeros_padded / reference_name_length))

        bin_count = np.bincount(coverage)
        probability = bin_count / bin_count.sum()
        shannon_entropy = -np.sum(probability*np.log2(probability))

        zr = zero_runs(coverage)
        if zr[0][0] == 0:
            if zr[-1][-1] == coverage.shape[0]:
                temp = zr[:, 1] - zr[:, 0]
                zr = np.concatenate((zr, np.atleast_2d(np.array([0, temp[0] + temp[-1]]))))
        percent_max_uncovered_region = np.max(zr[:, 1] - zr[:, 0]) / reference_name_length

        largest_pileup = np.max(coverage)

        results = AlignmentFeatures(
                hits=hits,
                percent_coverage=percent_coverage,
                expected_coverage=expected_coverage,
                percent_padded_coverage=percent_padded_coverage,
                shannon_entropy=shannon_entropy,
                percent_max_uncovered_region=percent_max_uncovered_region,
                largest_pileup=largest_pileup
            )
        yield results


def gen_fasta_features(fasta: Path) -> Generator[FastaFeatures, None, None]:
    with open(fasta) as inf:
        for header, seq in read_fasta(inf):
            seq = seq.strip().upper()
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
