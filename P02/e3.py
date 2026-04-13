from Client0 import Client

IP = "127.0.0.1"
PORT = 8081

c = Client(IP, PORT)


print("Sending a message to the server...")
response = c.talk("Testing!!!")
print(f"Response: {response}")