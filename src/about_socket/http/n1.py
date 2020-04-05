#coding:utf-8
#from BaseHTTPServer import HTTPServer,BaseHTTPRequestHandler  #py2
from http.server import BaseHTTPRequestHandler,HTTPServer  #py3

import json

class TodoHandle(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
    def do_GET(self):
        response={
            'status':'success',
            'data':'hello from server'
        }
        message=json.dumps(response)
        self._set_headers()
        self.wfile.write(message.encode())

    def do_POST(self):
        length=int(self.headers['Content-length'])
        post_values=json.loads(self.rfile.read(length))
        print(post_values)
        response={
            'status':'success',
            'data':'server got your post data'
        }
        self._set_headers()
        self.wfile.write(json.dumps(response).encode())

if __name__=="__main__":
    # Start a simple server, and loop forever
    server=HTTPServer(('localhost',3333),TodoHandle)
    print("Starting server,use <Ctrl-C> to stop")
    server.serve_forever()


