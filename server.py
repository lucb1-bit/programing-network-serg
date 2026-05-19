import http.server
import socketserver
import http.client
import json
from pathlib import Path
import termcolor
from urllib.parse import parse_qs, urlparse
from Seq_class import Seq
import jinja2 as j

def read_html_file(filename):
    contents = Path("html/" + filename).read_text()
    contents = j.Template(contents)
    return contents

SERVER = 'rest.ensembl.org'
PORT = 8080
socketserver.TCPServer.allow_reuse_address = True

class TestHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        termcolor.cprint(self.requestline, 'green')
        url_path = urlparse(self.path)
        path = url_path.path
        arguments = parse_qs(url_path.query)

        if path == "/":
            contents = Path('Final-Project/html/index.html').read_text()

        elif path == "/listSpecies":
            conn = http.client.HTTPSConnection(SERVER)
            limit = arguments.get('limit', [None])[0]
            endpoint = "/info/species?content-type=application/json"
            try:
                conn.request("GET", endpoint)
                response = conn.getresponse()
                if response.status == 200:
                    data = json.loads(response.read().decode("utf-8"))
                    data_list = data["species"]
                    name_list = []
                    if limit == None:
                        limit = len(data_list)
                    for specie in data_list[0:int(limit)]:
                        name_list.append(specie["common_name"])
                    contents = read_html_file("limit.html").render(name={"name": name_list},limit={"limit": int(limit)},total={"total": len(data_list)})
            except ConnectionRefusedError:
                print("ERROR! Cannot connect to the Server")
                exit()

        elif path == "/karyotype":
            conn = http.client.HTTPSConnection(SERVER)
            species = arguments.get( "species", [None])[0]
            endpoint = "/info/assembly/"+(str(species).replace(" ", "%20"))+"?content-type=application/json"
            try:
                # we send the request GET
                conn.request("GET", endpoint)
                # we received the response
                response = conn.getresponse()
                if response.status == 200:
                    data = json.loads(response.read().decode("utf-8"))
                    data_list = data["karyotype"]
                    if species == None:
                        contents = Path("Final-Project/html/error.html").read_text()
                    else:
                        contents = read_html_file("karyotype.html").render(name={"name": data_list})
                else:
                    contents = Path("Final-Project/html/error.html").read_text()
            except ConnectionRefusedError:
                print("ERROR! Cannot connect to the Server")
                exit()

        elif path == "/chromosomeLength" :
            conn = http.client.HTTPSConnection(SERVER)
            species = arguments.get("species", [None])[0]
            chromo = arguments.get("chromo", [None])[0]
            endpoint = "/info/assembly/" + (str(species).replace(" ", "%20")) + "?content-type=application/json"
            try:
                # we send the request GET
                conn.request("GET", endpoint)
                # we received the response
                response = conn.getresponse()
                if response.status == 200:
                    data = json.loads(response.read().decode("utf-8"))
                    data_list = data["top_level_region"]
                    if species == None or chromo == None:
                        contents = Path("Final-Project/html/error.html").read_text()
                    else:
                        for gen in data_list:
                            if gen["name"] == chromo:
                                length = int(gen["length"])
                                contents = read_html_file("length.html").render(number={"number": length})
                else:
                    contents = Path("Final-Project/html/error.html").read_text()
            except ConnectionRefusedError:
                print("ERROR! Cannot connect to the Server")
                exit()
        else:
            contents = Path('Final-Project/html/error.html').read_text()

        self.send_response(200)
        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', str(len(str.encode(contents))))
        self.end_headers()
        self.wfile.write(str.encode(contents))
        return

#PROGRAM
Handler = TestHandler
s = Seq()
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("Serving at PORT", PORT)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("")
        print("Stopped by the user")
        httpd.server_close()