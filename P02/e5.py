from Client0 import Client
from Seq1 import Seq

IP = "212.128.254.243"
PORT = 8081
c = Client(IP, PORT)
gene = "FRAT1"

print(f"Connection to SERVER at {IP}, PORT: {PORT}")

s1 = Seq()
s1.seq_read_fasta(gene)
msg= "Sending the " +gene+" Gene to the server..."
response = c.talk(msg)
print(f"To Server: {msg}")
print(f"From Server:\n{response}")
print(f"Gene {gene} : {str(s1)}")

list_sequence = s1.list_seq()

n = 1
for f in list_sequence:
    msg2 = "Fragment " + str(n) + ":" + str(f)
    if n<6:
        print(msg2)
        c.talk(msg2)
    n += 1