import sys
import xlsxwriter

c_sample = str(sys.argv[1])
chr_sample = open(c_sample, "r")
description = []
header = []
info = []
Info = []
d_INFO = {}
row = 1

for line in chr_sample:
    if line.startswith("##"):
        description.append(line.strip())
    elif line.startswith("#"):
        header += line.strip().split("\t")
    else:
        info = line.strip().split("\t")
        Info.append(info)
# 나눠야함

WB = xlsxwriter.Workbook("{chr_sample}.xlsx")
wSam = WB.add_worksheet({chr_sample})
wdes = WB.add_worksheet("description")

WB.use_zip64()
chr_sample.close()
WB.close()
