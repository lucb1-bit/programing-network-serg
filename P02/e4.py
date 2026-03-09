from Client0 import Client
from Seq1 import Seq

IP = "212.128.254.53"
PORT = 8081
c = Client(IP, PORT)

genes = ["U5", "FRAT1", "ADA"]

print(f"Connection to SERVER at {IP}, PORT: {PORT}")

for gene in genes:
    print(f"Sending the {gene} Gene to the server...")
    s1 = Seq()
    s1.seq_read_fasta(gene)
    print(f"To Server: {str(s1)}")

    response = c.talk(str(s1))
    print(f"From Server:\n{response}")