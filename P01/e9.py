from Seq1 import Seq

s1 = Seq()
s1.seq_read_fasta("sequences/U5.txt")

print(f"\nSequence 1: (Length: {s1.len()}) {s1} \n Bases: {s1.countB()} \n Rev: {s1.reverse()} \n Comp: {s1.seq_complement()}")