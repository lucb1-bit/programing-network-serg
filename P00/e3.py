from Seq0 import seq_read_fasta, seq_len
FOLDER = "../P00/sequences/"
genes = ["U5", "ADA", "FRAT1", "FXN"]

for gene in genes:
    filename = FOLDER + gene + ".txt"

    seq = seq_read_fasta(filename)
    length = seq_len(seq)
    print("Gene", gene, "-> Length:", length)