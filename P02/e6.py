from Client0 import Client
from Seq1 import Seq

IP = "212.128.254.243"
PORT = 8080
PORT2 = 8081
c1 = Client(IP, PORT)
c2 = Client(IP, PORT2)
print(f"Connection to SERVER at {IP}, PORT: {PORT}")
print(f"Connection to SERVER at {IP}, PORT: {PORT2}")
gene = "FRAT1"

s1 = Seq()
s1.seq_read_fasta(gene)
msg= "Sending the " +gene+" Gene to the server..."
c1.talk(msg)
c2.talk(msg)
print(f"Gene {gene} : {str(s1)}")

list_sequence = s1.list_seq()

n = 1
for f in list_sequence:
    msg2 = "Fragment " + str(n) + ":" + str(f)
    if n<11:
        if n % 2 != 0:
            print(msg2)
            c1.talk(msg2)
        else:
            print(msg2)
            c2.talk(msg2)
    n += 1