import http.client
import json

gene_names = ["FRAT1", "ADA", "FXN", "RNU6-269P", "MIR633",
              "TTTY4C", "RBMY2YP", "FGFR3", "KDR", "ANK2"]

# Create the dictionary we need
genes = {}

server = 'rest.ensembl.org'
conn = http.client.HTTPSConnection(server)

print("Buscando identificadores en Ensembl...\n")

try:
    for name in gene_names:
    # we build the endpoint
    endpoint = f"/lookup/symbol/homo_sapiens/{name}?content-type=application/json"

    conn.request("GET", endpoint)
    response = conn.getresponse()

    if response.status == 200:
        data = json.loads(response.read().decode("utf-8"))
        # we subtract the Id from the json response
        gene_id = data['id']
        # we added in the dictionary
        genes[name] = gene_id
        print(f"Gene: {name}. Id: {gene_id}")
    else:
        print(f"Error finding {name}: {response.status}")

except ConnectionRefusedError:
    print("ERROR! Cannot connect to the Server")
    exit()

