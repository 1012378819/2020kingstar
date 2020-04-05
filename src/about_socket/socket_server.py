#socket类的实例需要三个参数，第一个参数是地址族（默认是socket.AF_INET），第二个是流（socket.SOCK_STREAM,默认值）或数据报（socket.SOCK_DGRAM）套接字
#第三个是使用的协议(默认是0)
#套接字是程序（进程）之间进行通信的信息通道，可能会通过网络来通信，socket模块给提供了对客户端和服务器端套接字的低级访问功能，服务器套接字会在指定的端口
#监听客户端的连接，而客户机是直接连接的
import socket
s=socket.socket()
host=socket.gethostname()
port=1234
s.bind((host,port))
s.listen(5)
while True:
    c,addr=s.accept()
    print('get connection from',addr)
    c.send(bytes('thank you for connecting',encoding='utf-8'))
    c.close()