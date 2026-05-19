import http.client
import json
import termcolor
from Seq_class import Seq

# server and gen data
SERVER = "localhost:8080"
endpoint= f"/lookup/symbol/homo_sapiens/{name}?content-type=application/json"

    # Establish the connection
conn = http.client.HTTPSConnection(SERVER)
print(f"Connecting to server: {SERVER}")

    try:
        # we send the request GET
        conn.request("GET", endpoint)
        # we received the response
        response = conn.getresponse()
        print(f"Response received!: {response.status} {response.reason}\n")

        if response.status == 200:
            data = json.loads(response.read().decode("utf-8"))
            # we subtract the Id from the json response
            gene_id = data['id']
            termcolor.cprint("Gene: ", 'green')
            print(name)

            try:
                endpoint_1 = f"/sequence/id/{gene_id}?content-type=application/json"
                conn.request("GET", endpoint_1)
                response = conn.getresponse()
                if response.status == 200:
                    # Convert JSON into a dictionary
                    data = json.loads(response.read().decode("utf-8"))
                    fasta=data['seq']
                    s = Seq()
                    s1= Seq(fasta)
                    # The description is in desc
                    termcolor.cprint("Description:", 'green')
                    print(f"{data['desc']}")
                    # the sequence is in seq
                    termcolor.cprint("Total lengh:", 'green')
                    print(f"{s1.len()}")
                    print(f"{s1.percentage(s1.count())}")
                    termcolor.cprint("Most frequent base:", 'green')
                    print(f"{s1.most_freq()}")
                else:
                    print(f"Error: The gen cant be found (Status: {response.status})")
            except ConnectionRefusedError:
                print("ERROR! Cannot connect to the Server")
                exit()
        else:
            print(f"Error finding {name}: {response.status}")
    except ConnectionRefusedError:
        print("ERROR! Cannot connect to the Server")
        exit()

