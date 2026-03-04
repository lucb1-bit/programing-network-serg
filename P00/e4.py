from Seq0 import seq_read_fasta, seq_count_base

FOLDER = "../P00/sequences/"
genes = ["U5", "ADA", "FRAT1", "FXN"]
bases = ["A", "C", "T", "G"]

for g in genes:
    print("\nGene", g + ":")
    filename = FOLDER + g + ".txt"
    seq = seq_read_fasta(filename)

    for b in bases:
        count = seq_count_base(seq, b)
        print(" ", b + ":", count)