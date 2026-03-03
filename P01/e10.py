from Seq1 import Seq
FOLDER = "sequences/"
genes = ["U5", "ADA", "FRAT1", "FXN"]

for gene in genes:
    filename = FOLDER + gene + ".txt"
    s1 = Seq()
    s1.seq_read_fasta(filename)
    print(f"Gene: {gene} {s1.most_freq()}")
