from pathlib import Path
from process_exons import get_exons_from_file, all_bases
from sequence import seq_bases

file_seq4 = "../SEQUENCES/ADA.txt"
file_seq5 = "../SEQUENCES/ADA_EXONS.txt"
file_contents4 = Path(file_seq4).read_text()
file_contents5 = Path(file_seq5).read_text()

body_seq = seq_bases(file_contents4)
exons= all_bases(file_contents5)
exons_list = get_exons_from_file(exons)
max_bases = 44652852


print("Exon  |Long.  |Start       |End")

order = 1
for ex  in exons_list:
    final = body_seq.find(ex)
    length = len(ex)
    initial = (final + length) -1
    start = max_bases - initial
    end = max_bases - final
    print(f"{order:<5} | {length:<5} | {start:<10} | {end}")
    order += 1
