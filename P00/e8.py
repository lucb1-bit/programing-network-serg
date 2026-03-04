from Seq0 import seq_read_fasta,most_freq

FOLDER = "../P00/sequences/"
genes = ["U5", "ADA", "FRAT1", "FXN"]

for g in genes:
    filename = FOLDER + g + ".txt"
    seq = seq_read_fasta(filename)

    print("Gene",g,": Most frequent base: ", most_freq(seq))


