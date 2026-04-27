import http.client
import json
class Seq:
    def __init__(self, bases=None):
        if bases == None:
            self.bases = "NULL"
        else:
            isvalid = self.is_valid(bases)
            if isvalid == True:
                self.bases = bases
            elif isvalid == False:
                self.bases = "Invalid Sequence"

    def __str__(self):
        return self.bases

    def len(self):
        if (self.bases == "NULL") or (self.bases == "Invalid Sequence"):
            return 0
        else:
            return len(self.bases)

    def is_valid(self, bases):
        valid_bases = {'A', 'C', 'G', 'T'}
        for b in bases:
            if b not in valid_bases:
                return False
        return True

    def count(self):
        bases_dict = {'A':0, 'C':0, 'T':0, 'G':0}
        if self.bases == "NULL" or self.bases == "Invalid Sequence":
            bases_dict = {'A':0, 'C':0, 'T':0, 'G':0}
        else:
            for b in self.bases:
                if b in bases_dict:
                    bases_dict[b] += 1
        return bases_dict

    def percentage(self,n_bases):
        total = self.len()
        for b in n_bases:
            n_bases [b] = f"""{n_bases [b]}  ({round((n_bases [b] / total * 100),2)}%) """

        res = ""
        for item, value in n_bases.items():
            res += f"{item}: {value}\n "
        return res

    def most_freq(self):
        freq = self.count()
        most_dict = {}
        most = 0
        for f in freq:
            if freq[f] > most:
                most = freq[f]
                bs = f
                most_dict = {bs: most}
            elif freq[f] == most:
                most_dict[f] = most
        return most_dict


# server and gen data
SERVER = 'rest.ensembl.org'
# Endpoint for sequence by ID
name = input("Enter gene name: ")
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
        print(f"Gene: {name}. Id: {gene_id}")

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

                print(f"Description: {data['desc']}")
                # the sequence is in seq
                print(f"Total lengh: {s1.len()}")
                print(f"{s1.percentage(s1.count())}")
                print(f"Most frequent base:{s1.most_freq()}")
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

