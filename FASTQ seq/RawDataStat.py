import sys
import gzip
from typing import no_type_check

sample_name = str(sys.argv[1])

line_idx = 0
total_base = ""
q_over20 = 0
q_over30 = 0
A_base_count = 0
C_base_count = 0
G_base_count = 0
T_base_count = 0
N_base_count = 0
filename = gzip.open(sample_name, "rb")

for line in filename:
    line = str(line, "utf-8")
    line_idx += 1
    if line_idx % 4 == 2:
        total_base += line.strip()
        A_base_count += line.count("A")
        C_base_count += line.count("C")
        G_base_count += line.count("G")
        T_base_count += line.count("T")
        N_base_count += line.count("N")
    elif line_idx % 4 == 0:
        for q in line:
            score = ord(q) - 33
            if score >= 20:
                q_over20 += 1
            if score >= 30:
                q_over30 += 1


read_count = line_idx // 4
total_base_count = len(total_base)
q20 = q_over20 / total_base_count * 100
q30 = q_over30 / total_base_count * 100
n_percent = N_base_count / total_base_count
GC_percent = (G_base_count + C_base_count) / total_base_count

print(
    f"{sample_name}\t{total_base_count}\t{read_count}\t{n_percent}\t{GC_percent}\t{q20}\t{q30}"
)
print("SampleName : " f"{sample_name}")
print("Total A : " f"{A_base_count}")
print("Total C : " f"{C_base_count}")
print("Total G : " f"{G_base_count}")
print("Total T : " f"{T_base_count}")
print("Total N : " f"{N_base_count}")
print("Total Q30 : " f"{q_over30}")
print("Total Q20 : " f"{q_over20}")
print("Q30 Bases : " f"{q30}")
print("Q20 Bases : " f"{q20}")

gzip.open(sample_name, "rb").close()

