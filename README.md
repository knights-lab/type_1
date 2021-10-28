# type_1

The tool `type_1` is a computational pipeline for classifying presence-absence in whole-genome shotgun metagenomic datasets.

## Installation
The installation instructions is streamlined for Linux systems at this time.
This package requires anaconda, which is a system agnostic package and virtual environment manager.
Follow the installation instructions for your system at <http://conda.pydata.org/miniconda.html>.


### The conda way (personal install)
1. Follow the steps 1 and 2 of <https://bioconda.github.io/>
2. Run the following commands in a terminal:
```
conda create -n type_1 -c knights-lab -c bioconda -c conda-forge type_1
source activate type_1
```
    
### Development Installation

1. Run the following commands in a terminal:
```
conda create -n type_1 -c knights-lab -c bioconda -c conda-forge type_1 python pip
source activate type_1
```

2. Remove `type_1` and install via the github master branch. This will keep all the conda dependencies installed.
```
conda remove type_1 --force
pip install git+https://github.com/knights-lab/type_1.git --no-cache-dir --upgrade
```

Optional: You can reinstall to the newest git version of `type_1` at anytime via the command:
```
pip install git+https://github.com/knights-lab/type_1.git --no-cache-dir --upgrade
```


### Database creation GTDB202
```
# Download the GTDB metadata for bacteria
wget https://data.gtdb.ecogenomic.org/releases/release202/202.0/bac120_metadata_r202.tar.gz
tar -xvf bac120_metadata_r202.tar.gz

# Download the GTDB metadata for archaea
wget https://data.gtdb.ecogenomic.org/releases/release202/202.0/ar122_metadata_r202.tar.gz
tar -xvf ar122_metadata_r202.tar.gz

# Build the database features
type_1 database-fasta ../combined_seqs.fna ./bac120_metadata_r202.tsv ./ar122_metadata_r202.tsv ./db_features.csv
```
