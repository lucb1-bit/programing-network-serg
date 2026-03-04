from Seq1 import Seq

s1 = Seq()
s2 = Seq("ACTGA")
s3 = Seq("PPP")

print(f"\nSequence 1: (Length: {s1.len()}) {s1} \n Bases: {s1.countB()} \n Rev: {s1.reverse()} \n Comp: {s1.seq_complement()}")
print(f"Sequence 2: (Length: {s2.len()}) {s2} \n Bases: {s2.countB()} \n Rev: {s2.reverse()} \n Comp: {s2.seq_complement()}")
print(f"Sequence 3: (Length: {s3.len()}) {s3} \n Bases:{s3.countB()} \n Rev: {s3.reverse()} \n Comp: {s3.seq_complement()}")