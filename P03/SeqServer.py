import socket
from termcolor import colored
from Seq_class import Seq

PORT = 8080
IP = "127.0.0.1"

#crear un socket
ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

#establecer el socket con la IP y el puerto que quieres
ls.bind((IP, PORT))

#poner a escuchar al socket
ls.listen()

print("Seq Server running")

seq_example = ["GGCTTGTTTTTCTTGGACAGATTCATGCTGAAGCTCAAGTTTTTAAGAGGAGTTTAGCAT","CCTAAAAAAAGCCCCCCCTGGCAGGGAAGCGAACTCTGATCATCCTGGTGACACATGGAA","ATACTGTCCACTATACTAACAAAGACTAGCGTGCTGTTGGATATGTCAAGCGTGGGTGGA","CACTTTCTGCCAGCAGTCTTACCAAACCGAAGCCAAGCCATTCCTCCTTAAGACAGGCAG","AGTCAGACATGTAATAAAAACAACGACCGATGGGTTCAGTCCAAAGGGCAAACTGTAGTT","TCTGCTGGTTATAGTCACCCTCAAAACCTTTGGCTGTTACCAAGGACTGGGCTCTAATCT","GTCTGATGTCCTAATAACACAATTTTACATGGTGACATCACTGCAGCTGTGAACATGTGG","ATATATTTGTCTTAACCAAAGACTGCACCTCTTTCTGTGTGACCTCATTCTGTACTGCGT","AATGCTTCGATGCCTTCCTTTCAACAAAGTAGGATTACAAGGCCAACGTGCCTTGCAGTC","ACCCTTGCCGAACATTGTGCTGTGTATGGCCAACTGCTCTGATTAAGCAGCATAGTGTTA"]

while True:

    print("Waiting for connections...")

    cs, client_ip_port = ls.accept()

    msg = cs.recv(2048).decode().strip()
    parts = msg.split()
    command = parts[0]

    print(colored(command,"green"))

    if command == "PING":

        response = "OK!\n"
        print(response)

    elif command == "GET":

        n = int(parts[1])
        response = seq_example[n] + "\n"
        print(response)

    elif command == "INFO":

        seq = Seq(parts[1])
        total = seq.len()
        n_bases = seq.count()
        percentage = seq.percentage(n_bases)
        response = f"""Sequence: {seq} \nTotal length: {total} \n{percentage}"""
        print(response)


    elif command == "COMP":
        seq = Seq(parts[1])
        response = seq.seq_complement() + "\n"
        print(response)

    elif command == "REV":
        seq = Seq(parts[1])
        response = seq.reverse() + "\n"
        print(response)

    elif command == "GENE":
        gene_valid = ["U5","ADA","FRAT1","FXN","RNU6_269P"]
        seq = Seq()
        gene = parts[1]

        if gene in gene_valid:
            filename = f"SEQUENCES/{gene}.txt"
            response = seq.seq_read_fasta(filename)
            print(response)
        else:
            response = "ERROR\n"
            print(response)

    else:

        response = "ERROR\n"
        print(response)

    cs.send(response.encode())
    cs.close()
