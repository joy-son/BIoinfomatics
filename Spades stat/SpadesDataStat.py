import sys
from typing import no_type_check

sample_name = str(sys.argv[1])
with open(sample_name, "r") as filename:
    file = filename.readlines()
    cSeq = 0  # Sequence count
    tSeq = []  # total Sequence
    lSeq = []  # length Sequence
    n50 = 0
    l50 = 0

    for line in file:
        lines = line.strip()
        if lines.startswith(">"):
            cSeq += 1
        elif not lines.startswith(">"):
            tSeq.append(lines.strip())
            lSeq.append(len(lines))
        seq = "".join(tSeq)

    lSeq.sort(reverse=True)  # (원래되있지만)큰순서대로

    for sum in lSeq:
        n50 += sum
        if len(seq) / 2 <= n50:
            break
        l50 += 1
    N50 = lSeq[l50]
    L50 = l50 + 1 #last itself

print(
    f"{sample_name}\t{cSeq}\t{len(seq)}\t{N50}\t{L50}\t{lSeq[0]}\t{lSeq[-1]}\t{len(seq)/cSeq}"
)
print("SampleName : " f"{sample_name}")
print("Number of contigs : " f"{cSeq}")
print("Total contigs bases : " f"{len(seq)}")
print("N50 : " f"{N50}")
print("L50 : " f"{L50}")
print("Longest : " f"{lSeq[0]}")
print("Shortest : " f"{lSeq[-1]}")
print("Average length : " f"{len(seq)/cSeq}")