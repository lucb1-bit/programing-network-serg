from Seq1 import Seq

s1 = Seq()
s2 = Seq("ACTGA")
s3 = Seq("PPP")

print(f"Sequence 1: (Length: {s1.len()}) {s1} \n {s1.countB()}")
print(f"Sequence 2: (Length: {s2.len()}) {s2} \n {s2.countB()}")
print(f"Sequence 3: (Length: {s3.len()}) {s3} \n {s3.countB()}")

