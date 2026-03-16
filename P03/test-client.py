from Client0 import Client

IP = "127.0.0.1"
PORT = 8080

c = Client(IP, PORT)
print(f"Connection to SERVER at {IP}, PORT: {PORT}\n")

print("* Testing PING")
print(c.talk("PING"))

print("* Testing GET")
seq = c.talk("GET 0")
print(seq)

print("* Testing INFO")
print(c.talk(f"INFO {seq}"))

print("* Testing COMP")
print(c.talk(f"COMP {seq}"))

print("* Testing REV")
print(c.talk(f"REV {seq}"))

genes = ["U5","ADA","FRAT1","FXN","RNU6_269P"]

print("* Testing GENE")

for g in genes:
    print("GENE", g)
    print(c.talk(f"GENE {g}"))