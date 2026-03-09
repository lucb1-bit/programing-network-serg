from Client0 import Client

IP = "212.128.254.243"
PORT = 8081

c = Client(IP, PORT)


print("Sending a message to the server...")
response = c.talk("Testing!!!")
print(f"Response: {response}")