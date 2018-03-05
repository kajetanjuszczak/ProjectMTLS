export BLASTDB=/mnt/d/inne/uniref90

cd ../datasets/SingleFastaForPSSM
for entry in *.fasta
do
psiblast -query $entry -evalue 0.01 -db uniref90.fasta -num_iterations 3  -out ../PSSMDB/$entry.psiblast -out_ascii_pssm ../PSSMasci/$entry.pssm -num_threads=8
echo "done"
done
