from Client0 import Client
from Seq1 import Seq

IP = "212.128.254.53"
PORT = 8081
c = Client(IP, PORT)

genes = ["U5", "FRAT1", "ADA"]

for gene in genes:
    print(f"Sending the {gene} Gene to the server...")
    s1 = Seq()
    s1.seq_read_fasta(gene)
    str_s1=str(s1)
    response = c.talk(str_s1)
    print(f"Response: {response}")
