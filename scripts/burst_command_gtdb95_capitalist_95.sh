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
