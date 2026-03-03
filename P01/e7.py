from Seq1 import Seq

s1 = Seq()
s2 = Seq("ACTGA")
s3 = Seq("PPP")

print(f"Sequence 1: (Length: {s1.len()}) {s1} \n Bases: {s1.countB()} \n Rev: {s1.reverse()}")
print(f"Sequence 2: (Length: {s2.len()}) {s2} \n Bases: {s2.countB()} \n Rev: {s2.reverse()}")
print(f"Sequence 3: (Length: {s3.len()}) {s3} \n Bases:{s3.countB()} \n Rev: {s3.reverse()}")