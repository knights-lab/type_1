for file in fnas/*.fna;
    do
    DIRECTORY=filter_per_sample/$(basename ${file})
    if [ ! -d "$DIRECTORY" ]; then
        shogun filter --input ${file} --output  ${DIRECTORY} --database /mnt/btrfs/data/shogun/gtdb_95 --alignment True --threads 40;
    fi
done
