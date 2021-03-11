for ix in (10 100 1000 10000 100000 1000000);
  do
  for file in ../b6_capitalist_split_by_sample/*.b6;
      do
      python /mnt/nvidia/pkr/code/type_1/type_1/main.py features-alignment /mnt/btrfs/data/gtdb_95/gtdb_genomes_reps_r95/db_features.fixed.extra.csv ${file} $(basename ${file}).${ix}.extra.csv --newick-tree /mnt/btrfs/data/gtdb_95/gtdb_genomes_reps_r95/r95.gtdb.tree --num-bins ${ix} &
  done
done
