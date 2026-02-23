from Seq0 import seq_read_fasta,seq_complement

FOLDER = "../P00/sequences/"
gene = "U5"
filename = FOLDER + gene + ".txt"


seq = seq_read_fasta(filename)
fragment = seq[:20]
comp = seq_complement(fragment)

print("Gene", gene + ":")
print("Frag:", fragment)
print("Comp:", comp)