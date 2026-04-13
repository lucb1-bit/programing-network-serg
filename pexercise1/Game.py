import socket
import NumberGuesser
PORT = 8080
IP = "127.0.0.1"

# create an INET, STREAMing socket
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind((IP, PORT))
serversocket.listen()

while True:
    # accept connections from outside
    print("Waiting for connections at {}, {} ".format(IP, PORT))
    (clientsocket, address) = serversocket.accept()

    # Print the connection number
    print("CONNECTION: From the IP: {}".format(address))


    # Read the message from the client, if any
    msg = clientsocket.recv(2048).decode("utf-8")
    print("Message from client: {}".format(msg))

    # Send the message. Esto es un mensaje del servidor al cliente
    message = "Give a number\n"
    send_bytes = str.encode(message)
    # We must write bytes, not a string
    clientsocket.send(send_bytes)
    clientsocket.close()

#creo numero secreto