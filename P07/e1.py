import http.client
import json

SERVER = 'rest.ensembl.org'
ENDPOINT = '/info/ping'
PARAMS = '?content-type=application/json'
URL = SERVER + ENDPOINT + PARAMS

print()
print(f"Server: {SERVER}")
print(f"URL: {URL}")

# Connect with the server
conn = http.client.HTTPSConnection(SERVER)

try:
    conn.request("GET", ENDPOINT + PARAMS)
    response = conn.getresponse()
    print(f"Response received!: {response.status} {response.reason}")

    if response.status == 200:
        data_json = response.read().decode("utf-8")
        data = json.loads(data_json)

        if data.get('ping') == 1:
            print()
            print("PING OK! The database is running!")
except ConnectionRefusedError:
    print("ERROR! Cannot connect to the Server")
    exit()