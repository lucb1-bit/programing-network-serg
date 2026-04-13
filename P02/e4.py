from Client0 import Client
from Seq1 import Seq

IP = "127.0.0.1"
PORT = 8081
c = Client(IP, PORT)

genes = ["U5", "FRAT1", "ADA"]

print(f"Connection to SERVER at {IP}, PORT: {PORT}")

for gene in genes:
    s1 = Seq()
    s1.seq_read_fasta(gene)
    msg= "Sending the " +gene+" Gene to the server..."
    response = c.talk(msg)
    print(f"To Server: {msg}")
    print(f"From Server:\n{response}")


    print(f"To Server: {str(s1)}")
    response = c.talk(str(s1))
    print(f"From Server:\n{response}")