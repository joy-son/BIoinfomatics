#!/bin/bash

for i in $(ls *.fastq.gz)
do
                python3 RawDataStat.py $i
done

