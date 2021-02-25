# type_1

Location of the file on teraminx
/project/flatiron2/ben/projects/type_1

/project/flatiron2/ben/projects/data/hmp_mock_community/shi7_learning_tminx/coverage-200527.txt

Working with MSI for building the new RefSeq database:

https://sites.google.com/site/knightslabinternal/methods/get-a-persistent-interactive-node-msi

And some other basic commands: https://www.msi.umn.edu/content/job-submission-and-scheduling-pbs-scripts

Run the command:
qsub jobs/ram1t.pbs
qstat -u hillm096

https://github.com/knights-lab/BURST/blob/master/embalmlets/bin/Readme_utils.txt ```

# Viruses
wget ftp://ftp.ncbi.nlm.nih.gov/genomes/refseq/viral/assembly_summary.txt -O- > assembly_summary.txt
# Archaea
wget ftp://ftp.ncbi.nlm.nih.gov/genomes/refseq/archaea/assembly_summary.txt -O- >> assembly_summary.txt
# Bacteria
wget ftp://ftp.ncbi.nlm.nih.gov/genomes/refseq/bacteria/assembly_summary.txt -O- >> assembly_summary.txt
# Protozoa
wget ftp://ftp.ncbi.nlm.nih.gov/genomes/refseq/protozoa/assembly_summary.txt -O- >> assembly_summary.txt
# Fungi
wget ftp://ftp.ncbi.nlm.nih.gov/genomes/refseq/fungi/assembly_summary.txt -O- >> assembly_summary.txt

# Rip out rep/ref and make sure it is latest and Full
awk -F "\t" '($5 == "representative genome" || $5 == "reference genome") && $14=="Full" && $11=="latest"{print $20}' assembly_summary.txt > ftpdirpaths

# Add the filepaths to the genomes
awk 'BEGIN{FS=OFS="/";filesuffix="genomic.fna.gz"}{ftpdir=$0;asm=$10;file=asm"_"filesuffix;print ftpdir,file}' ftpdirpaths > ftpfilepaths

# Download the files on 16 threads
cat ftpfilepaths | xargs -n 1 -P 16 wget -q --retry-connrefused --waitretry=1 --read-timeout=20 --timeout=15 -t 99

# Make the new directory
mkdir fna & mv *.gz fna & cd fna & printf '%s\0' *.gz | xargs -r0 -n 1 -P 16 gunzip

# Linearize the genomes
../lingenome . AllGenomes.fasta AllPlasmids.fasta HEADFIX
```

# Database
```

# Database
# Mock Communities

## fastq dumps
```
fastq-dump --skip-technical  --readids --dumpbase --split-files --clip
fastq-dump --skip-technical  --readids --dumpbase --split-files --clip SRR8073716:
fastq-dump --skip-technical  --readids --dumpbase --split-files --clip ERR3200809;
fastq-dump --skip-technical  --readids --dumpbase --split-files --clip ERR2835738;
fastq-dump --skip-technical  --readids --dumpbase --split-files --clip ERR2935805;
fastq-dump --skip-technical  --readids --dumpbase --split-files --clip ERR2984773;
```

## fastq dumps dnanexus
```
https://dl.dnanex.us/F/D/X3kyPyv0jQyJQYyQKJgyvG6z3fz9ZJZ12kP0zqVf/strains2_CHALLENGE_truth.txt?inline
https://dl.dnanex.us/F/D/KVQYkZGb9V8yJ01v7BQfJzJXQF0bbzK670qBxQ3p/CS_1_1.fastq.gz
https://dl.dnanex.us/F/D/4V6PQvqp5xFYbXGQj8JzVZBvZJyf8zJjZJVGZyF0/CS_1_2.fastq.gz
https://dl.dnanex.us/F/D/jbf85846j5Zb8ZB14ff0pJBg1jZpQpJ4Xv41FPjB/CS_2_1.fastq.gz
https://dl.dnanex.us/F/D/6BBZkGBGf3g7BFJ0YfG51gkzp0j8Gy09YgzzPQYq/CS_2_2.fastq.gz
https://dl.dnanex.us/F/D/JVqpGZ72Zk5pbF2gbQ43y0qX7YQ3pBzJzbJG9jkX/CS_3_1.fastq.gz
https://dl.dnanex.us/F/D/9bjbF5f5f69VzPP1p47xvJy2b948JKv3769bKZX3/CS_3_2.fastq.gz
https://dl.dnanex.us/F/D/BkbqbxBQQ5GB4xBz31gxV2X0Yz3pKQB14gQBBQ31/CS_4_1.fastq.gz
https://dl.dnanex.us/F/D/8zvb48vqKgjPG8FjKVZX6XvQ7fZ4JYk3GBvq9fzb/CS_4_2.fastq.gz
```


```
# Consolidate and download (xargs used for parallel download/extraction and also to enable entire download)
awk 'BEGIN{FS=OFS="/";filesuffix="genomic.fna.gz"}{ftpdir=$0;asm=$10;file=asm"_"filesuffix;print ftpdir,file}' ftpdirpaths > ftpfilepaths
cat ftpfilepaths | xargs -n 1 -P 16 wget -q --retry-connrefused --waitretry=1 --read-timeout=20 --timeout=15 -t 99
printf '%s\0' *.gz | xargs -r0 -n 1 -P 16 gunzip
```

## location of files
```
/project/flatiron2/ben/projects/type_1/bin/burst15
/project/flatiron2/ben/projects/type_1/data/zymo/ERR2935805
/project/flatiron2/ben/projects/type_1/data/zymo/ERR2984773
/project/flatiron2/ben/projects/type_1/data/bmock_12/SRR8073716
/project/flatiron2/ben/projects/type_1/data/gis_20/ERR3200809
/project/flatiron2/ben/projects/type_1/data/gis_20/ERR2835738
/project/flatiron2/ben/projects/type_1/data/mosaic/shi7_cmd.sh
/project/flatiron2/ben/projects/type_1/data/mosaic/CS_4
/project/flatiron2/ben/projects/type_1/data/mosaic/CS_3
/project/flatiron2/ben/projects/type_1/data/mosaic/CS_2
/project/flatiron2/ben/projects/type_1/data/mosaic/CS_1
/project/flatiron2/ben/projects/type_1/data/mbarc_26/SRR3656745
```


sra_filename

```
** Strain contimanation
*** Features
**** decontam - https://microbiomejournal.biomedcentral.com/articles/10.1186/s40168-018-0605-2
***** read-length test -> frequency should be independent of total read counts
****** build two linear regression models, one with a coefficient of total reads one without see which one has lower
 sum of squared errors
****** does not work well on low biomass
***** contiminate read test
****** chi-square test, hypothesis is that class (control sample vs experimental sample) has no influence on the fre
quency of the feature (e.g sample)
       *****
****** works well on low biomass
**** CheckM - https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4484387/
***** check if an assembled strain has the core genes for survival
**** Mosaic Strains Challenge - https://www.nature.com/articles/s41467-019-13549-9#Sec13
***** False Positive identification is found in Supplementary Note 5
****** evenness of coverage
****** edit distance graph (HOPS)
****** DNA damage patterns PMDTools
***** Great coverage graph found here https://static-content.springer.com/esm/art%3A10.1038%2Fs41467-019-13549-9/Med
iaObjects/41467_2019_13549_MOESM1_ESM.pdf
**** HOPS: automated detection and authentication of pathogen DNA in archaeological remains - https://genomebiology.
biomedcentral.com/articles/10.1186/s13059-019-1903-0
***** Negative difference ratio
****** build histogram of edit distance bins with number of reads as the y-axis
****** take the difference between each consecutive bins
****** divide the sum of all absoluate negative differences by the sum of absoluate all differences
****** Intuition is that the edit distance histogram should have a negative slope. That is the, number of reads with
 higher distances should be changed
***** Also take a look at CG ratios
*** Mock communities
**** HMP Mock Community
***** SRR17902- even community
****** https://www.ncbi.nlm.nih.gov/sra/SRX055380[accn]
***** SRR172903 - staggered community
****** https://www.ncbi.nlm.nih.gov/sra/SRX055381[accn]
**** Dual Indexing Mock Communityy
Paper link https://link.springer.com/referenceworkentry/10.1007/978-1-4614-6418-1_54-1
Data link https://mothur.org/MiSeqDevelopmentData/
```


## Mock Communities align to RefSeq 201
/project/flatiron/data/shogun/rep201_ab/refseq_s3333_d301.{acx, edx}

```
# 

```

### Finished the first alignment yesterday
```
/project/flatiron2/projects/type_1/data/mock/mock_communities/zymo/ERR2935805/allpath.r201.b6
```

# Features
## SHOGUN features
* max_uncovered_region - longest stretch of nucleotides in clade that are not covered
* percent_max_uncovered_region - max_uncovered_region as a percentage of genome length
* percent_of_genome_covered - percent of genome covered
* median_genome_size - median size of the genome in the clade
* hits_in_clade - raw number of reads that hit the sequence
* unique_counts_of_clade - unique shears of the clade
* expected_coverage - the expected coverage of the genome given the reads hit it (measure of evenness)
* ratio_covered_over_expected - ratio of coverage over expected 

## Mosaic Features
### NCBI Team Approach
* padded_alignment - coverage with padding
* coverage_evenness - coverage of the genome should be relatively uniform

### One Codex
* kmer_distribution - kmer distribution of reads that hit the clade should match the kmer distribution of the full genome

## ChecKM
* core_genes_for_survival - core genes of the genome covered (might be too difficult to use)

## decontam 
* read_length_test - frequency across samples should be independent of total reads counts of the sample
* contaminate_read_test - (control vs experimental sample) frequency should be independent

## Features derived from combined_seqs.fna
genome_length
gc_distribution


# 


```
general:
        fasta: blank.txt
        taxonomy: taxmap.tsv
        shear: sheared_bayes.tsv
burst: burst/combined_seqs
filter: filter/combined_seqs.filtered

```

### Working with the alignments

Location on superglass
```
/mnt/btrfs/data/type_1/mock_communities
```

Steps for completion
* download
* quality control
* filter
* align
* labels

Downloading the strains:

# https://www.ncbi.nlm.nih.gov/datasets/docs/command-line-start/

This didn't work, trying the next thing.


