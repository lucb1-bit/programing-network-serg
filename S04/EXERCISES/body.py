from pathlib import Path
file_seq2 = "../SEQUENCES/U5.txt"
file_contents2 = Path(file_seq2).read_text()


def end_ofline(seq):
    i = seq.find("\n")
    valid_seq = seq[i:len(seq)]
    return valid_seq
print("Body of the U5.txt file:\n", end_ofline(file_contents2))