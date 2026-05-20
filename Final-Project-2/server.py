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

def ensembl(endpoint):
   #connection to ensemble
    try:
        conn = http.client.HTTPSConnection('rest.ensembl.org')
        conn.request("GET", f"{endpoint}?content-type=application/json")
        response = conn.getresponse()
        if response.status == 200:
            return json.loads(response.read().decode("utf-8"))
    except Exception:
        return None

SERVER = 'rest.ensembl.org'
PORT = 8080
socketserver.TCPServer.allow_reuse_address = True

class TestHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        termcolor.cprint(self.requestline, 'green')
        url_path = urlparse(self.path)
        path = url_path.path
        arguments = parse_qs(url_path.query)

        contents = ""
        raw_data = None

        json_data = arguments.get('json', [None])[0]
        if json_data == '1':
            is_json = True
        else:
            is_json = False

        if path == "/":
            contents = Path('html/index.html').read_text()

        elif path == "/listSpecies":
            limit = arguments.get('limit', [None])[0]
            data = ensembl("/info/species")
            if data:
                data_list = data["species"]
                name_list = []
                if limit == None:
                    limit = len(data_list)
                for specie in data_list[0:int(limit)]:
                    name_list.append(specie["common_name"])
                contents = read_html_file("limit.html").render(name={"name": name_list},limit={"limit": int(limit)},total={"total": len(data_list)})
                raw_data = {"species": name_list, "limit": int(limit), "total": len(data_list)}

        elif path == "/karyotype":
            species = arguments.get( "species", [None])[0]
            data = ensembl("/info/assembly/"+(str(species).replace(" ", "%20")))
            if data:
                data_list = data["karyotype"]
                if species == None:
                    contents = Path("html/error.html").read_text()
                else:
                    contents = read_html_file("karyotype.html").render(name={"name": data_list})
                    raw_data = {"species": species, "karyotype": data_list}
            else:
                contents = Path("html/error.html").read_text()

        elif path == "/chromosomeLength" :
            species = arguments.get("species", [None])[0]
            chromo = arguments.get("chromo", [None])[0]
            data = ensembl("/info/assembly/" + (str(species).replace(" ", "%20")))
            if data:
                data_list = data["top_level_region"]
                if species == None or chromo == None:
                    contents = Path("html/error.html").read_text()
                else:
                    for gen in data_list:
                        if gen["name"] == chromo:
                            length = int(gen["length"])
                            contents = read_html_file("length.html").render(number={"number": length})
                            raw_data = {"species": species, "chromosome": chromo, "length": length}
            else:
                contents = Path("html/error.html").read_text()

        elif path in ["/geneLookup", "/geneSeq", "/geneInfo", "/geneCalc"]:
            gene = arguments.get('gene', [None])[0]
            data = ensembl("/lookup/symbol/homo_sapiens/"+str(gene))
            if gene == None or data == None:
                contents = Path("html/error.html").read_text()
            else:
                if path == "/geneLookup":
                    gene_id = data['id']
                    contents = read_html_file("geneLookup.html").render(ident={"ident": gene_id},name={"name": gene})
                    raw_data = {"gene": gene, "id": gene_id}
                elif path == "/geneSeq":
                    description = ensembl(f"/sequence/id/{data['id']}")
                    seq = description["seq"]
                    contents = read_html_file("geneSeq.html").render(seq={"seq":seq}, name={"name": gene})
                    raw_data = {"gene": gene,"seq": seq}
                elif path == "/geneInfo":
                    start = data["start"]
                    end = data["end"]
                    name = data["display_name"]
                    ident = data["id"]
                    reg = data["seq_region_name"]
                    length = int(end)-int(start)+1
                    contents = read_html_file("geneInfo.html").render(start={"start":start}, name={"name": name}, end={"end": end}, len={"len": length},id={"id": ident},reg={"reg": reg})
                    raw_data = {"gene": name, "id": ident, "chromosome": reg, "start": start, "end": end,"length": length}
                elif path == "/geneCalc":
                    description = ensembl(f"/sequence/id/{data['id']}")
                    seq = Seq(description["seq"])
                    total_len = seq.len()
                    total_bases= seq.count()
                    percentage_bases = seq.percentage(total_bases)
                    contents = read_html_file("geneCalc.html").render(len={"len":total_len}, percent={"percent": percentage_bases},name={"name": gene})
                    raw_data = {"gene": gene, "length": total_len, "percentages": percentage_bases}

        elif path == "/geneList":
            chromo = arguments.get("chromo", [None])[0]
            start = arguments.get("start", [None])[0]
            end = arguments.get("end", [None])[0]

            if chromo and start and end:
                try:
                    conn = http.client.HTTPSConnection('rest.ensembl.org')
                    conn.request("GET", f"/overlap/region/human/{chromo}:{start}-{end}?content-type=application/json&feature=gene&feature=transcript&feature=cds&feature=exon")
                    response = conn.getresponse()
                    genes_found = []
                    if response.status == 200:
                        data= json.loads(response.read().decode("utf-8"))
                        if data is not None:
                            for gen_dict in data:
                                for item,value in gen_dict.items():
                                    if item == "external_name":
                                        if value not in genes_found:
                                            genes_found.append(value)
                            contents = read_html_file("geneList.html").render(name={"name": genes_found},chromo={"chromo":chromo},start={"start":start},end={"end": end})
                            raw_data = {"chromosome": chromo, "start": start, "end": end, "genes": genes_found}
                except Exception:
                    contents = Path('html/error.html').read_text()
            else:
                contents = Path('html/error.html').read_text()

        elif path == "/compare_genes":
            g1 = arguments.get("g1", [None])[0]
            g2 = arguments.get("g2", [None])[0]
            if g1 and g2:
                try:
                    conn = http.client.HTTPSConnection('rest.ensembl.org')
                    conn.request("GET", f"/lookup/id/{g1}?expand=1?content-type=application/json")
                    response = conn.getresponse()
                    if response.status == 200:
                        data1= json.loads(response.read().decode("utf-8"))
                except Exception:
                    contents = Path('html/error1.html').read_text()
                try:
                    conn = http.client.HTTPSConnection('rest.ensembl.org')
                    conn.request("GET", f"/lookup/id/{g2}?expand=1?content-type=application/json")
                    response = conn.getresponse()
                    if response.status == 200:
                        data2= json.loads(response.read().decode("utf-8"))
                        if data1 and data2 is not None:
                            name1 = data1["display_name"]
                            name2 = data2["display_name"]
                            contents = read_html_file("exam1.html").render(name1={"name1": name1},
                                                                          name2={"name2": name2}, g1={"g1": g1},
                                                                          g2={"g2": g2})
                        else:
                            contents = Path('html/error1.html').read_text()

                except Exception:
                    contents = Path('html/error1.html').read_text()

            else:
                contents = Path('html/error1.html').read_text()

        else:
            contents = Path('html/error.html').read_text()



        self.send_response(200)
        if is_json and raw_data is not None:
            self.send_header('Content-Type', 'application/json')
            contents = json.dumps(raw_data)
            response_bytes = contents.encode('utf-8')
        else:
            self.send_header('Content-Type', 'text/html')
            if not contents:
                contents = Path('html/error.html').read_text()
            response_bytes = contents.encode('utf-8')

        self.send_header('Content-Length', str(len(response_bytes)))
        self.end_headers()
        self.wfile.write(response_bytes)
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