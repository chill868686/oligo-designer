#

#设计的oligo拼接、标注位置、计算overlap TM值




from Bio.SeqUtils import MeltingTemp as mt
from Bio.Seq import Seq

mystring1 = 'CCTGTCCCCCATGCTCCAGGCAC'
mystring2 = 'AGGTGGAGGAAGGGGCAGCCTGTGCCTGGAGCATGGGGGACAG'
mystring2 = mystring2[::-1]
myseq1 = Seq(mystring1)
myseq2 = Seq(mystring2)
print(str(myseq1))
print("."*0+str(myseq2))
print('%0.2f' % mt.Tm_NN(myseq1,c_seq=myseq2,shift=-1,dnac1=10,dnac2=10,nn_table=mt.DNA_NN4,Na=0,K=0,Tris=0,Mg=4,dNTPs=1,saltcorr=7))
#print('%0.2f' % mt.salt_correction(Na=50,K=0,Tris=10,Mg=8, method=7))