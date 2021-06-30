/usr/bin/env bash
# Archaea/Bacteria Database Building
# Download the assembly summary for each of the files
wget https://ftp.ncbi.nlm.nih.gov/genomes/refseq/archaea/assembly_summary.txt -O- > assembly_summary.txt
wget https://ftp.ncbi.nlm.nih.gov/genomes/refseq/bacteria/assembly_summary.txt -O- >> assembly_summary.txt

# Grab the latest and full genomes
awk -F "\t" '($5 == "" || $5 == "reference genome") && $14=="Full" && $4!="" && $11=="latest"{print $20}' assembly_summary.txt >> ftpdirpaths

# Get the ftpfilepaths from the dir paths
awk 'BEGIN{FS=OFS="/";filesuffix="genomic.fna.gz"}{ftpdir=$0;asm=$10;file=asm"_"filesuffix;print ftpdir,file}' ftpdirpaths | sed 's/ftp:/https:/' > ftpfilepaths

awk 'BEGIN{FS=OFS="/";filesuffix="wgsmaster.gbff.gz"}{ftpdir=$0;asm=$10;file=asm"_"filesuffix;print ftpdir,file}' ftpdirpaths | sed 's/ftp:/https:/' > ftpfilewgspaths

# Download the files
cat ftpfilewgspaths | xargs -n 1 -P 16 wget -q --retry-connrefused --waitretry=1 --read-timeout=20 --timeout=15 -t 40
cat ftpfilepaths | xargs -n 1 -P 16 wget -q --retry-connrefused --waitretry=1 --read-timeout=20 --timeout=15 -t 40

# download an assembly
fastq-dump --skip-technical  --readids --dumpbase --split-files --clip SAMEA2771239;

cat /mnt/nvidia/pkr/code/type_1/data/biosamples.500.txt | xargs -n 1 -P 1 fastq-dump --skip-technical --readids --dumpbase --split-files --clip
cat /mnt/nvidia/pkr/code/type_1/data/wgs_master.all.txt | xargs -n 1 -P 16 bio fetch



for line in $(cat /mnt/nvidia/pkr/code/type_1/data/biosamples.500.txt); do fastq-dump --skip-technical  --readids --dumpbase --split-files --clip ${line}; done
