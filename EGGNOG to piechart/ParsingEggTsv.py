import sys
import pandas as pd

sample = str(sys.argv[1])

t_sample = pd.read_csv(
    sample,
    sep="\t",
    engine="python",
    encoding="cp949",
    skiprows=4,
    skipfooter=3,
)
s_match = 0
m_match = 0
nohit = 0
l_cog = []
t_cog = []
a_cog = []
set_cog = []  # index생성
num = []
l_cnt = []
count = 0
d_cog = {
    "A": "RNA processing and modification",
    "B": "Chromatin structure and dynamics",
    "C": "Energy production and conversion",
    "D": "Cell cycle control, cell division, chromosome partitioning",
    "E": "Amino acid transport and metabolism",
    "F": "Nucleotide transport and metabolism",
    "G": "Carbohydrate transport and metabolism",
    "H": "Coenzyme transport and metabolism",
    "I": "Lipid transport and metabolism",
    "J": "Translation, ribosomal structure and biogenesis",
    "K": "Transcription",
    "L": "Replication, recombination and repair",
    "M": "Cell wall/membrane/envelope biogenesis",
    "N": "Cell motility",
    "O": "Posttranslational modification, protein turnover, chaperones",
    "P": "Inorganic ion transport and metabolism",
    "Q": "Secondary metabolites biosynthesis, transport and catabolism",
    "R": "General function prediction only",
    "S": "Function unknown",
    "R": "General function prediction only",
    "S": "Function unknown",
    "T": "Signal transduction mechanisms",
    "U": "Intracellular trafficking, secretion, and vesicular transport",
    "V": "Defense mechanisms",
    "W": "Extracellular structures",
    "Y": "Nuclear structure",
    "Z": "Cytoskeleton",
}
cog = t_sample.loc[:, "COG_category"]
total = len(cog)
l_cog = cog.values.tolist()

for i in l_cog:  # 노힛 카운트 및 제거, 싱글&멀티플 카운트 및 cog 한줄
    if i == "-":
        nohit += 1
    else:
        if len(i) == 1:
            s_match += 1
        else:
            m_match += 1
        t_cog.append(i)
        a_cog = "".join(t_cog)

for c in d_cog:
    count = a_cog.count(c)
    num.append([c, d_cog[c], count, round(count / len(a_cog) * 100, 2)])

figure = pd.DataFrame(num)  # 데이터프레임생성
figure.columns = ["Category", "Symbol", "Count", "Persentage(%)"]
figure.to_csv("figure.tsv", index=False, sep="\t")

sample = sample[3:]
## print
print(f"File name : {sample}")
print(f"Total query : {total}")
print(
    "Annotation :",
    s_match + m_match,
    "(%.2f%%)" % ((s_match + m_match) / total * 100),
)
print(
    "Single matched annotation :", s_match, "(%.2f%%)" % (s_match / total * 100)
)
print(
    "Multiple matched annotation :",
    m_match,
    "(%.2f%%)" % (m_match / total * 100),
)
print("No hit :", nohit, "(%.2f%%)" % (m_match / total * 100))
