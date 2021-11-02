## If you get a warning message, ModuleNotFoundError: No module named 'scipy'
## excute "pip install scipy"
from scipy.spatial import distance

fr = open("./TT_Set_A.csv","r")
fw_dt = open("./HammingDistance.txt","w")
fw_fq = open("./HammingFrequency.txt","w")

l_indexset = []
l_fq = []
d_fq = {}

fw_dt.write("index_set") #index sets 생성
lines = fr.readlines()[1:]
for line in lines:
    line = line.strip().split(",")
    l_indexset.append(f"{line[1]}+{line[2]}")
    fw_dt.write(f"\t{line[1]}+{line[2]}") #distance file column 생성

for row in l_indexset:
    fw_dt.write(f"\n{row}") #distance file row 생성
    i_row = [list(row.split("+")[0]), list(row.split("+")[1])]
    for col in l_indexset: 
        i_col = [list(col.split("+")[0]), list(col.split("+")[1])]
        fw_dt.write(f"\t={int(distance.hamming(i_row[0],i_col[0])*len(i_row[0]))}+{int(distance.hamming(i_row[1],i_col[1])*len(i_row[1]))}") #distance result 생성
        l_fq.append(f"{int(distance.hamming(i_row[0], i_col[0]) * len(i_row[0]))} + {int(distance.hamming(i_row[1], i_col[1]) * len(i_row[1]))}") #frequency []

fw_fq.write("HammingDist_i7\tHammingDist_i5\tIndex_Count") #frequency file column 생성
for key in l_fq:
    d_fq[key] = d_fq.get(key, 0) + 1  # frequency {} 생성        
else:
    fw_fq.write(f"\n{key.split('+')[0]}\t{key.split('+')[1]}\t{d_fq[key]}") #frequency result 생성

fr.close()
fw_dt.close()
fw_fq.close()
