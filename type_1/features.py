from pathlib import Path
from typing import Tuple, Generator
import csv
from collections import Counter, defaultdict
import re

from copy import deepcopy
from ete3 import Tree
import numpy as np
import pandas as pd

from type_1 import logger
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


def get_coverage(length_of_genome: int, num_nonzeros: int) -> float:
    if length_of_genome <= num_nonzeros:
        return 1.
    else:
        coverage = num_nonzeros / length_of_genome
        return coverage


def get_shannon_entropy(coverage: np.ndarray) -> float:
    bin_count = np.bincount(coverage)
    probability = bin_count[bin_count > 0] / bin_count.sum()
    shannon_entropy = -np.sum(probability*np.log2(probability))
    return shannon_entropy


def get_binned_coverage(alignments: np.ndarray, genome_length: int, num_bins=1_000) -> np.ndarray:
    # bins = np.linspace(0, coverage.shape[0], num=num_bins + 1, endpoint=True, dtype=np.int)
    # counts = np.diff(bins)
    #
    # binned_hits = np.add.reduceat(coverage, bins[:-1])
    # coverage = get_coverage(num_bins, binned_hits)
    # return means, coverage
    bins = np.linspace(0, genome_length, num=num_bins + 1)
    hist, _ = np.histogram(alignments, bins=bins)
    return hist


def gen_blast_features(
    alignment_allpath: Path,
    df_database_features: pd.DataFrame,
    padding: int = 100,
    num_bins: int = 10_000,
) -> Generator[AlignmentFeatures, None, None]:
    d_reference_name_to_alignments = defaultdict(list)
    with open(alignment_allpath) as inf:
        inf_csv = csv.reader(inf, delimiter="\t")
        for row in inf_csv:
            # [
            #   'ERR2935805.R2_218359', read_name
            #   'GCF_000196035.1', assembly_accession
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
            assembly_accession = row[1]
            alignment = sorted((int(row[8]) - 1, int(row[9]) - 1))
            d_reference_name_to_alignments[assembly_accession].append(alignment)

    for assembly_accession, alignments in d_reference_name_to_alignments.items():
        # get the reference length
        query = df_database_features.query(f"assembly_accession == '{assembly_accession}'")
        if query.shape[0] != 1:
            print(f"ERROR WITH QUERY {assembly_accession}")
            print(query)
            continue

        reference_name_length = query.total_genome_length.iloc[0]

        coverage = np.zeros(shape=reference_name_length, dtype=int)
        padded_coverage = np.zeros(shape=reference_name_length, dtype=int)

        np_alignments_beginning = np.array([alignment[0] for alignment in alignments], dtype=int)
        binned_coverage = get_binned_coverage(np_alignments_beginning, reference_name_length, num_bins=num_bins)

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

        nonzeros = (coverage > 0).sum()

        # num zeros
        hits = len(alignments)
        percent_coverage = get_coverage(reference_name_length, nonzeros)

        expected_coverage = get_expected_coverage(reference_name_length, np.sum(coverage))

        # binned coverage stats
        nonzeros_binned = (binned_coverage > 0).sum()
        percent_binned_coverage = get_coverage(num_bins, nonzeros_binned)

        # num zeros padded
        nonzeros_padded = (padded_coverage > 0).sum()
        percent_padded_coverage = get_coverage(reference_name_length, nonzeros_padded)

        # windows for bins
        shannon_entropy = get_shannon_entropy(coverage)

        zr = zero_runs(coverage)
        if zr[0][0] == 0:
            if zr[-1][-1] == coverage.shape[0]:
                temp = zr[:, 1] - zr[:, 0]
                zr = np.concatenate((zr, np.atleast_2d(np.array([0, temp[0] + temp[-1]]))))

        # TODO: sometimes this is 2?
        percent_max_uncovered_region = np.max(zr[:, 1] - zr[:, 0]) / reference_name_length

        largest_pileup = np.max(coverage)
        largest_padded_pileup = np.max(padded_coverage)
        largest_binned_pileup = np.max(binned_coverage)

        results = AlignmentFeatures(
                assembly_accession=assembly_accession,
                hits=hits,
                percent_coverage=percent_coverage,
                mean_coverage=np.mean(coverage),
                sd_coverage=np.std(coverage),
                percent_padded_coverage=percent_padded_coverage,
                mean_padded_coverage=np.mean(padded_coverage),
                sd_padded_coverage=np.std(padded_coverage),
                percent_binned_coverage=percent_binned_coverage,
                mean_binned_coverage=np.mean(binned_coverage),
                sd_binned_coverage=np.std(binned_coverage),
                expected_percent_coverage=expected_coverage,
                shannon_entropy=shannon_entropy,
                percent_max_uncovered_region=percent_max_uncovered_region,
                largest_pileup=largest_pileup,
                largest_padded_pileup=largest_padded_pileup,
                largest_binned_pileup=largest_binned_pileup
            )
        yield results


def gen_fasta_features(fasta: Path) -> Generator[FastaFeatures, None, None]:
    with open(fasta) as inf:
        for header, seq in read_fasta(inf):
            seq = seq.strip().upper()
            total_genome_length = genome_length(seq)
            freqs = nucleotide_frequency(seq)
            ns, num_groups = longest_consecutive_ns(seq)

            # we can't do this, as burst will never align to ns because of penalties
            ungapped_genome_length = total_genome_length - freqs["N"]
            gc_content = (freqs["G"] + freqs["C"]) / total_genome_length

            results = FastaFeatures(
                total_genome_length=total_genome_length,
                ungapped_genome_length=ungapped_genome_length,
                num_n_groups=num_groups,
                consecutive_ns=ns,
                gc_content=gc_content,
                assembly_accession=header
            )
            yield results


def read_tree(nw_path: Path) -> Tree:
    with open(nw_path) as inf:
        nw_tree = inf.readlines()

    t = Tree(nw_tree[0], format=3, quoted_node_names=True)
    return t


def get_tree_based_features(df_features: pd.DataFrame, nw_path: Path) -> pd.DataFrame:
    tree = read_tree(nw_path)

    pruned_tree = deepcopy(tree)

    # leaves_names = set([_.name for _ in tree.get_leaves()])

    leaves_in_tree = set(df_features.assembly_accession)

    # leaves_to_prune = leaves_names.difference(leaves_in_tree)

    pruned_tree.prune(leaves_in_tree, preserve_branch_length=True)

    results = []
    for leave in leaves_in_tree:
        closest, dist = pruned_tree.get_closest_leaf(leave)
        if closest.name != leave:
            dist = tree.get_distance(leave, closest.name)
            top_distance = tree.get_distance(leave, closest.name, True)
        else:
            logger.warning(f"Nearest neighbor to node {leave} is itself!")
            dist = 0
            top_distance = 0
        results.append([leave, closest.name, dist, top_distance])
    df_tree = pd.DataFrame(results, columns=["assembly_accession", "tree_closest_assembly_accession", "tree_dist", "tree_top_dist"])
    df_merged = pd.merge(df_tree, df_features, how="left", left_on="tree_closest_assembly_accession", right_on="assembly_accession", suffixes=('', "_DROP"))
    df_merged = df_merged.drop(columns=["assembly_accession_DROP"])
    df_merged_2 = pd.merge(df_merged, df_features, how="inner", on="assembly_accession", suffixes=('', "_tree_x"))
    df_merged_2.columns = ["tree_" + col.replace("_tree_x", "") if col.endswith("_tree_x") else col for col in df_merged_2.columns]
    return df_merged_2
