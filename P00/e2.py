from Seq0 import seq_read_fasta

FOLDER = "../P00/sequences/"
FILENAME = "U5.txt"

file = FOLDER + FILENAME

seq = seq_read_fasta(file)

print("The first 20 bases are:", seq[0:20])