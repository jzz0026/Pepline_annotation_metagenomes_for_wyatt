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
  for i in $(ls *.tab | cut -d '.' -f 1) ; do sbatch -t 2880 --mincpus=1 --mem=6G -D $PWD -J get_querylist --wrap="cat $i.tab | awk -F \" \" '{print $1}' | sed 's/_.*$//g' | uniq | sed '$d' > $i.querylist" ; done


sbatch -t 2880 --mincpus=4 --mem=24G -D $PWD -J test_grep --wrap="cat 1047887_Browns_ThreeSqA_D1_extract_CH4_hmm.querylist | xargs -I {} grep {} 1047887_Browns_ThreeSqA_D1.fasta -A 1 > 
1047887_Browns_ThreeSqA_D1_extract_test.grep"
