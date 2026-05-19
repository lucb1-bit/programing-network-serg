import http.client
import json

SERVER_LOCAL = "localhost:8080"


def request_json(endpoint):
    print(f"Requesting data from: http://{SERVER_LOCAL}{endpoint}")
    try:
        conn = http.client.HTTPConnection(SERVER_LOCAL)
        conn.request("GET", endpoint)
        response = conn.getresponse()

        print(f"SERVER RESPONSE Status: {response.status} {response.reason}")
        if response.status == 200:
            #json data interpreted
            data_dict = json.loads(response.read().decode("utf-8"))
            print("JSON DATA RECEIVED:")
            print(json.dumps(data_dict))
        else:
            print(f"SERVER ERROR Error description: {response.read().decode('utf-8')}")
    except ConnectionRefusedError:
        print("ERROR! Cannot connect to the Server")
        exit()


# Test List Species
request_json("/listSpecies?limit=3&json=1")

# Test karyotype
request_json("/karyotype?species=shrew+mouse&json=1")

#Test Gene Lookup
request_json("/geneLookup?gene=ADA&json=1")

#Test Gene Info
request_json("/geneInfo?gene=FRAT1&json=1")

#Test Gene Overlap
request_json("/geneList?chromo=9&start=22125500&end=22136000&json=1")