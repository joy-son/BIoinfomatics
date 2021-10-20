#!/bin/bash

for i in $(ls | egrep '.tsv$|.csv$')
do 
                name=`echo ${i} | cut -d "." -f1`
                mkdir ${name}
                cd ${name}
                python3 ../ParsingEggTsv.py ../${i} | tee log.txt
                Rscript ../pie_chart.R
                cd ..              
done
