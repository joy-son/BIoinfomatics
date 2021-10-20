# drop sequences shorter than 1kb 
seqtk seq -L 1000 scaffolds.fasta > f_scaffolds.fasta

# change the header
sed -i s/NODE_/contig/g ./00.Raw/f_scaffolds.fasta ; sed s/_l/'\t'/g ./00.Raw/f_scaffolds.fasta | cut -f1 > ./01.Rename/fn_scaffold.fasta