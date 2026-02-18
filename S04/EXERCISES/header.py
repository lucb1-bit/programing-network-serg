from pathlib import Path
file_seq = "../SEQUENCES/RNU6_269P.txt"
file_contents = Path(file_seq).read_text()

header = file_contents.split('\n')
print("First line of the RNU6_269P.txt file:\n",header[0])


#def end_ofline(seq):
#  i = seq.find("\n")
#  valid_seq = seq[0:i]
#  return valid_seq
#print("First line of the RNU6_269P.txt file:\n", end_ofline(file_contents))""