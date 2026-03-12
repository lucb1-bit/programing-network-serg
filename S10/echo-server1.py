import socket
from termcolor import colored

PORT = 8080
IP = "212.128.254.60"

ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

ls.bind((IP, PORT))
ls.listen()

print("The server is configured!")

counter = 1
while True:
    # -- Waits for a client to connect
    print("Waiting for Clients to connect")
    (cs, client_ip_port) = ls.accept()

    print(f"CONNECTION {counter}. client IP, PORT:{client_ip_port}")
    counter +=1
    # -- Read the message from the client
    # -- The received message is in raw bytes
    msg_raw = cs.recv(2048)

    # -- We decode it for converting it
    # -- into a human-redeable string
    msg = msg_raw.decode()
    msg_green = colored(msg, "green")

    # -- Print the received message
    print(f"Message received: {msg_green}")

    # -- Send a response message to the client
    response ="ECHO:" + str(msg)
    # -- The message has to be encoded into bytes
    cs.send(response.encode())

    # -- Close the data socket
    cs.close()
