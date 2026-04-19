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

class TestHandler(http.server.BaseHTTPRequestHandler): 
    def do_GET(self):
        termcolor.cprint(self.requestline, 'green')
        url_path = urlparse(self.path)
        path = url_path.path
        arguments = parse_qs(url_path.query)
        if path == "/":
            contents = Path('html/form-1.html').read_text()
        elif path == "/echo":
            msg = arguments.get("msg", [""])[0]
            contents = read_html_file("form-e3.html").render(context={"todisplay": msg})
        else :
            contents = Path('html/error.html').read_text()
        self.send_response(200) 
        self.send_header('Content-Type', 'text/html') 
        self.send_header('Content-Length', len(str.encode(contents))) 
        self.end_headers() 
        self.wfile.write(str.encode(contents)) 
        return
    
Handler = TestHandler
with socketserver.TCPServer(("", PORT), Handler) as httpd: 
    print("Serving at PORT", PORT) 
    try: 
        httpd.serve_forever() 
    except KeyboardInterrupt: 
        print("") 
        print("Stopped by the user") 
        httpd.server_close()