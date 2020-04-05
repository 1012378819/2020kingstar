#coding:utf-8
import socket
import re
import sys
from multiprocessing import Process

#设置静态文件根目录
HTML_ROOT_DIR="./html"
#设置动态文件根目录
WSGI_PYTHON_DIR='./wsgitest'

class HTTPServer(object):
    def __init__(self):
        self.sever_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.sever_socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)

    def start(self):
        self.sever_socket.listen(12)
        while True:
            client_socket,client_addr=self.sever_socket.accept()
            print("[%s,%s]用户连接上了", client_addr)
            handle_client_process=Process(target=self.handle_client,args=(client_socket,))
            handle_client_process.start()
            client_socket.close()

    def start_response(self,status,headers):
        response_headers="HTTP/1.1"+status+"\r\n"
        for header in headers:
            response_headers+="%s: %s\r\n" %header

        self.response_headers=response_headers

    def handle_client(self,client_socket):
        """处理客户端请求"""
        request_data=client_socket.recv(1024)
        print("request_data",request_data)
        request_lines=request_data.splitlines()
        request_start_line=request_lines[0]
        file_name=re.match(r"\w+ +(/[^ ]*) ",request_start_line.decode("utf-8")).group(1)
        method=re.match(r"(\w+) +/[^ ]* ",request_start_line.decode("utf-8")).group(1)
        print(file_name)
        # 处理动态文件
        if file_name.endswith(".py"):
            try:
                m=__import__(file_name[1:-3])
            except Exception:
                self.response_headers="HTTP/1.1 404 Not Found\r\n"
                response_body="not found"
            else:
                env={
                    "PATH_INFO":file_name,
                    "METHOD":method
                }
                response_body=m.application(env,self.start_response)
            response=self.response_headers+"\r\n"+response_body
        #处理静态文件
        else:
            if '/'==file_name:
                file_name="/index.html"

            #打开文件，读取内容
            try:
                file=open(HTML_ROOT_DIR+file_name,'rb')
            except IOError:
                response_start_line="HTTP/1.1 404 Not Found\r\n"
                response_headers="Server:My server\r\n"
                response_body="The file is not found!"
            else:
                file_data=file.read()
                file.close()

                #构造响应数据
                response_start_line="HTTP/1.1 200 ok\r\n"
                response_headers="Server:My server\r\n"
                response_body=file_data.decode("utf-8")

            response=response_start_line+response_headers+"\r\n"+response_body
        #向客户端返回响应数据
        client_socket.send(bytes(response,"utf-8"))

        #关闭客户端连接
        client_socket.close()

    def bind(self,port):
        self.sever_socket.bind(("",port))

def main():
    sys.path.insert(1,WSGI_PYTHON_DIR)
    http_server=HTTPServer()
    http_server.bind(8000)
    http_server.start()

if __name__=="__main__":
    main()







