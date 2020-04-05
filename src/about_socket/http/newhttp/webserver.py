from http.server import HTTPServer,CGIHTTPRequestHandler

host=('localhost',8010)

WebServer=HTTPServer(host,CGIHTTPRequestHandler)
WebServer.serve_forever()