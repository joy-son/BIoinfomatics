sample=$1_blast.out

cat ${sample} | cut -f2 | uniq > log.txt

for i in $(cat log.txt)
do
	cat ${sample} | grep "${i}" | wc -l >> count.txt
	c=`cat ${sample} | grep "${i}" | wc -l`
	echo "${i}\t${c}" >> parsing.txt
done

cat parsing.txt
