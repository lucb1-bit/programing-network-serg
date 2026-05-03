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
            contents = Path('html/index.html').read_text()

        elif path == "/listSpecies":
            conn = http.client.HTTPSConnection(SERVER)
            msg_0 = arguments.get('msg_0', ['0'])[0]
            endpoint = "/info/species?content-type=application/json"
            try:
                # we send the request GET
                conn.request("GET", endpoint)
                # we received the response
                response = conn.getresponse()
                if response.status == 200:
                    data = json.loads(response.read().decode("utf-8"))
                    data_list = data["species"]
                    name_list = []
                    for specie in data_list[0:int(msg_0)]:
                        name_list.append(specie["common_name"])
                    contents = read_html_file("limit.html").render(name={"name": name_list},limit={"limit": int(msg_0)},total={"total": len(data_list)})
            except ConnectionRefusedError:
                print("ERROR! Cannot connect to the Server")
                exit()
        elif path == "/karyotype":
            msg_1 = arguments.get('n', ['0'])[0]
            contents = read_html_file("limit.html").render(context={"todisplay": msg_1}, context_1={"number": n})

        elif path == "/chromosomeLength" :
            msg_2 = arguments.get('gene', ['0'])[0]
            msg_3 = arguments.get('msg', ['0'])[0]
            genes = ["U5", "ADA", "FRAT1", "FXN", "RNU6_269P"]
            if gene in genes:
                gene_read= s.seq_read_fasta("SEQUENCES/"+gene+".txt")
                contents = read_html_file("limit.html").render(context={"todisplay": gene_read}, context_1={"gene": gene})

        elif path == "/operation":
            msg_2= arguments.get("op", [""])[0]
            msg_3 = arguments.get('msg', ['0'])[0]
            s1=Seq(msg)
            if op == "comp":
                res = s1.seq_complement()
            elif op == "info":
                n_bases = s1.count()
                res = s1.percentage(n_bases)
            elif op == "rev":
                res = s1.reverse()
            contents = read_html_file("operation.html").render(context={"op": op}, context_1={"result": res },context_2={"msg": msg })
        else:
            contents = Path('html/error.html').read_text()

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