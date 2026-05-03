import http.server
import socketserver
from pathlib import Path
import termcolor
from urllib.parse import parse_qs, urlparse
import jinja2 as j

def read_html_file(filename):
    contents = Path("html/" + filename).read_text()
    contents = j.Template(contents)
    return contents


PORT = 8080

socketserver.TCPServer.allow_reuse_address = True


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

    def reverse(self):
        reverse = ""
        if self.bases == "NULL" or self.bases == "Invalid Sequence":
            return self.bases
        else:
            reverse = ""
            for b in self.bases:
                reverse = b + reverse
            return reverse

    def seq_complement(self):
        base_dict = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
        replaced_seq = ""
        if self.bases == "NULL" or self.bases == "Invalid Sequence":
            return self.bases
        else:
            for b in self.bases:
                if b in base_dict:
                    replaced_seq += base_dict[b]
            return replaced_seq

    def seq_read_fasta(self,filename):
        filename = open(filename, "r")
        lines = filename.readlines()
        filename.close()

        seq_lines = lines[1:]
        sequence = ""
        for line in seq_lines:
            sequence += line.strip()
        self.bases = sequence
        return self.bases

class TestHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        termcolor.cprint(self.requestline, 'green')
        url_path = urlparse(self.path)
        path = url_path.path
        arguments = parse_qs(url_path.query)


        if path == "/":
            contents = Path('html/index.html').read_text()

        elif path in "/ping":
            contents = Path('html/ping.html').read_text()

        elif path == "/get":
            n = arguments.get('n', ['0'])[0]
            sequences = ["AAAA", "GGGG", "CCCC", "TTTT","AGTC"]
            seq = sequences[int(n)]
            contents = read_html_file("limit.html").render(context={"todisplay": seq}, context_1={"number": n})

        elif path == "/gene":
            gene = arguments.get('gene', ['0'])[0]
            genes = ["U5", "ADA", "FRAT1", "FXN", "RNU6_269P"]
            if gene in genes:
                gene_read= s.seq_read_fasta("SEQUENCES/"+gene+".txt")
                contents = read_html_file("limit.html").render(context={"todisplay": gene_read}, context_1={"gene": gene})
            else:
                contents = Path('html/error.html').read_text()

        elif path == "/operation":
            op = arguments.get("op", [""])[0]
            msg = arguments.get('msg', ['0'])[0]
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
        self.send_header('Content-Length', len(str.encode(contents)))
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