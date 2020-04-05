#SocketServer（py2）框架是一个同步的网络服务器基类
from http.server import BaseHTTPRequestHandler,HTTPServer

class Handler(BaseHTTPRequestHandler):
    def handle(self):
        addr=self.request.getpeername()
        print('get connection from ',addr)
        self.wfile.write('thank you for connecting')

server=HTTPServer(('',1234),Handler)
server.serve_forever()