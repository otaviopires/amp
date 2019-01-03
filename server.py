import http.server
import socketserver

PORT = 8201

Handler = http.server.SimpleHTTPRequestHandler
httpd = socketserver.TCPServer(("", PORT), Handler)

print(("Serving on ", PORT))
httpd.serve_forever()