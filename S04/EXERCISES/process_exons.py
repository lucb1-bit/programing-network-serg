from pathlib import Path

from sympy import sequence

file_seq4 = "../SEQUENCES/ADA_EXONS.txt"
file_contents4 = Path(file_seq4).read_text()

def all_bases(seq):
    final_seq = seq.replace("\n", "")
    final = final_seq.replace(" ", "")
    return final[1:len(final)]

def get_exons_from_file(seq):
    list_exon = seq.split(">")
    list_seq = []
    for ex in list_exon:
        initial=ex.find("coding")
        list_seq.append(ex[initial+6:len(ex)])
    return list_seq

sequence = all_bases(file_contents4)
apoe_exons = get_exons_from_file(sequence)
print(apoe_exons)
