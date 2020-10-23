#!/usr/bin/env bash
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
