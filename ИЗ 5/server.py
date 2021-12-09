import http.server as BaseHTTPServer
import http.server as CGIHTTPServer

server = BaseHTTPServer.HTTPServer
handler = CGIHTTPServer.CGIHTTPRequestHandler

server_address = ("localhost", 8000)

httpd = server(server_address, handler)
httpd.serve_forever()


