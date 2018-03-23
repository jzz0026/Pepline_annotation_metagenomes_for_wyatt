## README
1. Extract hmm domains from foam and transform fastq to fasta

  cd /global/projectb/scratch/jzz0026/wyatt_wetland # extract hmm domains of CPS and CH4only from foam

  python extract_hmm-CPS.py ## CPS domains
  
  python extract_hmm-CH4.py ## CH4 domains
  

2. ORF prediction for all metagenomes (results: *_orfs.fasta) 

  cd /global/projectb/scratch/jzz0026/wyatt_wetland/hmmsearch
  
  bash run_prodigal.sh
  

3. Run hmmsearch for all metagenomes (results: *.tab)

  write_scipt_to_fasta_prodigal_hmmsearch.ipynb # write script
  
  bash submit.sh
  

4. Transform hmm tab result into summary and filered table (results: *.result and *.summary)

  ls *.tab | xargs -I {} sbatch -t 2880 --mincpus=1 --mem=6G -D $PWD -J test --wrap="python Filter_count_hmm_result.py {}"
  
5. submit cmd to get query list

  for i in $(ls *.tab | cut -d '.' -f 1) ; do sbatch -t 2880 --mincpus=1 --mem=6G -D $PWD -J get_querylist --wrap="cat $i.tab | awk -F \" \" '{print $1}' | sed 's/_.*$//g' | sed '$d' | sort | uniq > $i.querylist" ; done

6. extract sequences from fasta file by matching header ID list

  for i in $(ls *.querylist | sed 's/_extract_CH4_hmm.querylist//') ; do sbatch -t 2880 --mincpus=1 --mem=6G -D $PWD -J test --wrap="module load bbtools/prod-v37.76 ; filterbyname.sh in=${i}.fasta names=${i}_extract_CH4_hmm.querylist include=t out=${i}_extract_CH4_hmm.fasta";  done


module unload gcc
module load gcc/6.3.0 

/global/projectb/scratch/jzz0026/tools/kaiju/bin/kaiju -t /global/projectb/scratch/jzz0026/tools/kaiju/kaijudb/nodes.dmp -f /global/projectb/scratch/jzz0026/tools/kaiju/kaijudb/kaiju_db_nr.fmi -z 32 -i Salt_Pond_MetaGSF2_A_D1_MG_DASTool_bins_concoct_out.23_orf.fa -o Salt_Pond_MetaGSF2_A_D1_MG_DASTool_bins_concoct_out.23.out

zhou
