for folder in ./*;
    do
    file=${folder}/combined_seqs.fna
    if [ -f "$file" ]; then
      python /mnt/nvidia/pkr/code/helix/helix/crop.py -f ${file} -o ${folder}/combined_seqs.300.200.fna --max_length 300 --min_length 50
      cat ${folder}/combined_seqs.300.200.fna >> combined_seqs.fna
      rm ${file}
      rm ${folder}/combined_seqs.300.200.fna
    fi
done
