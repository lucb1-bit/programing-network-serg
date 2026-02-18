from pathlib import Path
file_seq3 = "../SEQUENCES/ADA.txt"
file_contents3 = Path(file_seq3).read_text()

def all_bases(seq):
    i = seq.find("\n")
    valid_seq = seq[i+1:len(seq)]
    final_seq = valid_seq.replace("\n", "")
    final = final_seq.replace(" ", "")
    return final

sequence = all_bases(file_contents3)
print(sequence)
print("The total number of bases is :", len(sequence))