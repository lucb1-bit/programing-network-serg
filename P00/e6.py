from Seq0 import seq_read_fasta,seq_reverse

FOLDER = "../P00/sequences/"
gene = "U5"



filename = FOLDER + gene + ".txt"
seq = seq_read_fasta(filename)
fragment = seq[:20]
reverse = seq_reverse(seq,20)

print("Gene", gene)
print("Fragment: ", fragment)
print("Reverse: ", reverse)