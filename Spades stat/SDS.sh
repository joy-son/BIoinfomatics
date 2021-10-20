#!/bin/bash

for i in $(ls *.fasta)
do
                python3 SpadesDataStat.py $i
done

