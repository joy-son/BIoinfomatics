vcf=$1
chr=$2

cd ${vcf}
if [ ${chr} = "all" ];then
    for i in $(cat log.txt)
    do
    python3 ../vcf2xlsx.py $i.vcf
    done    
else
    do
    python3 ../vcf2xlsx.py $i.vcf
    done    
fi
