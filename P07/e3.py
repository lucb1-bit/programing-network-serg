import http.client
import json

# server and gen data
SERVER = 'rest.ensembl.org'
GENE_ID = "ENSG00000207552"
# Endpoint for sequence by ID
ENDPOINT = f"/sequence/id/{GENE_ID}?content-type=application/json"

# Establish the connection
conn = http.client.HTTPSConnection(SERVER)

print(f"Connecting to server: {SERVER}")

try:
    # we send the request GET
    conn.request("GET", ENDPOINT)

    # we received the response
    response = conn.getresponse()
    print(f"Response received!: {response.status} {response.reason}\n")

    if response.status == 200:
        # Decode response
        data_raw = response.read().decode("utf-8")
        # Convert JSON into a dictionary
        data = json.loads(data_raw)

        print(f"Gene: MIR633")
        # The description is in desc
        print(f"Description: {data['desc']}")
        # the sequence is in seq
        print(f"Sequence: {data['seq']}")
    else:
        print(f"Error: The gen cant be found (Status: {response.status})")

except ConnectionRefusedError:
    print("ERROR! Cannot connect to the Server")
    exit()