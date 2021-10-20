vcf=$1

mkdir ${vcf}
cd ${vcf}

cat ../${vcf}.vcf | cut -f1 | egrep '^chr' | uniq | tee log.txt

for chr in $(cat log.txt)
do
    cat ../${vcf}.vcf | egrep "^#" > $chr.vcf
    cat ../${vcf}.vcf | grep "^$chr" >> $chr.vcf
done
