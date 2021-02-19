/usr/bin/time -v burst15 \
 -t 140 \
 -q /scratch.global/ben/type_1/species_mc/filtered/combined_seqs.fna \
 -a /scratch.global/ben/gtdb/gtdb_s5000_d301.acx \
 -r /scratch.global/ben/gtdb/gtdb_s5000_d301.edx \
 -o /scratch.global/ben/type_1/species_mc/filtered/allpaths.b6 \
 -m ALLPATHS \
 -fr \
 -i 0.98 \
 --noprogress \
 > /scratch.global/ben/type_1/species_mc/filtered/allpath.gtdb95.log 2>&1



