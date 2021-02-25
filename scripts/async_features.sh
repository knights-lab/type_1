for file in ./*.b6;
    do
    python /mnt/nvidia/pkr/code/type_1/type_1/main.py features-alignment /mnt/btrfs/data/gtdb_95/gtdb_genomes_reps_r95/db_features.fixed.extra.csv ${file} ${file}.extra.tree.csv --newick-tree /mnt/btrfs/data/gtdb_95/gtdb_genomes_reps_r95/r95.gtdb.tree &
done
