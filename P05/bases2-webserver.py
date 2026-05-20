import socketserver
import http.server
import termcolor

IP = "127.0.0.1"
PORT = 8080

# -- This is for preventing the error: "Port already in use"
socketserver.TCPServer.allow_reuse_address = True

# Class with our Handler. It is a called derived from BaseHTTPRequestHandler
# It means that our class inherits all his methods and properties
class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        """This method is called whenever the client invokes the GET method
        in the HTTP protocol request"""

        # Print the request line
        termcolor.cprint(self.requestline, 'green')

        req = self.requestline
        lines = req.split('\n')
        req_line = lines[0]

        r = req_line.split(" ")
        base_list = ["/info/A", "/info/C", "/info/G", "/info/T"]
        if r[1] in base_list:
            name = "html" + r[1] + "exam.html"
            with open(name, "r") as f:
                body = f.read()
        elif r[1] == "/":
            with open("html/index.html", "r") as f:
                body = f.read()
        else:
            with open("html/error.html", "r") as f:
                body = f.read()

        # Generating the response message
        self.send_response(200)  # -- Status line: OK!

        # Define the content-type header:
        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', len(body.encode()))

        # The header is finished
        self.end_headers()

        # Send the response message
        self.wfile.write(body.encode())

        return

print("Server configured!")

# ------------------------
# - Server MAIN program
# ------------------------
# -- Set the new handler
Handler = TestHandler

# -- Open the socket server
with socketserver.TCPServer(("", PORT), Handler) as httpd:

    print("Serving at PORT", PORT)

    # -- Main loop: Attend the client. Whenever there is a new
    # -- clint, the handler is called
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("")
        print("Stopped by the user")
        httpd.server_close()