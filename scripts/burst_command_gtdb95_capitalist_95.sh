/usr/bin/time -v burst15 \
 -t 128 \
 -q /scratch.global/ben/type_1/species_mc/filtered/combined_seqs.300.50.fna \
 -a /scratch.global/ben/gtdb/gtdb_s5000_d301.acx \
 -r /scratch.global/ben/gtdb/gtdb_s5000_d301.edx \
 -o /scratch.global/ben/type_1/species_mc/filtered/capitalist.32.98.gtdb95.b6 \
 -m CAPITALIST \
 -fr \
 -i 0.98 \
 --noprogress \
 > /scratch.global/ben/type_1/species_mc/filtered/capitalist.32.98.gtdb95.log 2>&1

/usr/bin/time -v burst15 \
 -t 128 \
 -q /scratch.global/ben/type_1/species_mc/filtered/combined_seqs.300.50.fna \
 -a /scratch.global/ben/gtdb/gtdb_s5000_d301.acx \
 -r /scratch.global/ben/gtdb/gtdb_s5000_d301.edx \
 -o /scratch.global/ben/type_1/species_mc/filtered/capitalist.32.95.gtdb95.b6 \
 -m CAPITALIST \
 -fr \
 -i 0.95 \
 --noprogress \
 > /scratch.global/ben/type_1/species_mc/filtered/capitalist.32.95.gtdb95.log 2>&1

/usr/bin/time -v burst15 \
 -t 128 \
 -q /scratch.global/ben/type_1/combined_seqs.fna \
 -a /scratch.global/ben/gtdb/gtdb_s5000_d301.acx \
 -r /scratch.global/ben/gtdb/gtdb_s5000_d301.edx \
 -o /scratch.global/ben/type_1/capitalist.32.98.gtdb95.b6 \
 -m CAPITALIST \
 -fr \
 -i 0.98 \
 --noprogress \
 > /scratch.global/ben/type_1/capitalist.32.98.gtdb95.log 2>&1


/usr/bin/time -v burst15 \
 -t 128 \
 -q /home/cutle051/cutle051/projects/chemo/data/runs1234_hostfilt_combinedseqs.fna \
 -a /scratch.global/ben/gtdb/gtdb_s5000_d301.acx \
 -r /scratch.global/ben/gtdb/gtdb_s5000_d301.edx \
 -o /scratch.global/ben/type_1/capitalist.chemo.32.98.gtdb95.b6 \
 -m CAPITALIST \
 -fr \
 -i 0.98 \
 --noprogress \
 > /scratch.global/ben/type_1/capitalist.32.chemo.98.gtdb95.log 2>&1

shi7.py --input /mnt/btrfs/data/type_1/hmp/stool_test --adaptor TruSeq2 --output /mnt/btrfs/data/type_1/hmp/stool_test --flash False --allow_outies False --filter_qual 37 --trim_qual 34

/usr/bin/time -v burst15 \
 -t 128 \
 -q /scratch.global/ben/type_1/magic/Knights_Project_046/filter/combined_seqs.fna \
 -a /scratch.global/ben/gtdb/gtdb_s5000_d301.acx \
 -r /scratch.global/ben/gtdb/gtdb_s5000_d301.edx \
 -o /scratch.global/ben/type_1/magic/Knights_Project_046/filter/capitalist.32.98.gtdb95.b6 \
 -m CAPITALIST \
 -fr \
 -i 0.98 \
 --noprogress \
 > /scratch.global/ben/type_1/magic/Knights_Project_046/filter/capitalist.32.98.gtdb95.log 2>&1

/usr/bin/time -v burst15 \
 -t 128 \
 -q /scratch.global/ben/type_1/magic/Knights_Project_055/filter/combined_seqs.fna \
 -a /scratch.global/ben/gtdb/gtdb_s5000_d301.acx \
 -r /scratch.global/ben/gtdb/gtdb_s5000_d301.edx \
 -o /scratch.global/ben/type_1/magic/Knights_Project_055/filter/capitalist.32.98.gtdb95.b6 \
 -m CAPITALIST \
 -fr \
 -i 0.98 \
 --noprogress \
 > /scratch.global/ben/type_1/magic/Knights_Project_055/filter/capitalist.32.98.gtdb95.log 2>&1
