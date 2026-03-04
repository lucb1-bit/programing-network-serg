from Seq0 import seq_read_fasta,seq_count

FOLDER = "../P00/sequences/"
genes = ["U5", "ADA", "FRAT1", "FXN"]

for g in genes:
    filename = FOLDER + g + ".txt"

    seq = seq_read_fasta(filename)
    counter = seq_count(seq)

    print("Gene", g + ":", counter)