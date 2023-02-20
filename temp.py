from Bio import pairwise2
from Bio import Seq

s1 = Seq.Seq('ACCGGT')
s2 = Seq.Seq('ACGT')
alignments = pairwise2.align.globalxx(s1,s2)
for alignment in alignments:
    print(alignment)