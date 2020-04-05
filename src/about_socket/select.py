#1、当一个服务器与一个客户端通信时，来自客户端的数据可能是不连续的，异步处理方法：只处理在给定时间内真正要进行通信的客户端，
#不需要一直监听---只要监听（或读取）一会儿。然后把它放到其他客户端的后面
#2、异步I/O   select、poll(伸缩性更好，但只能在unix系统使用)
#3、select和poll这两个函数让你可以考虑一组连接并且能找出已经准备好读取或者写入的连接，这意味着能通过时间片轮转来为几个连接提供服务，
# 看起来像是同时处理多个连接
import socket,select

s=socket.socket()

host=socket.gethostname()
port=1111
s.bind((host,port))

s.listen(5)
inputs=[s]
while True:
    rs,ws,es=select.select(inputs,[],[])
    for r in rs:
        if r is s:
            c,addr=s.accept()
            print('gotconnection from',addr)
            inputs.append(c)

        else:
            try:
                data=r.recv(1024)
                disconnected=not data
            except socket.error:
                disconnected=True

            if disconnected:
                print(r.getpeername(),'disconnected')
                inputs.remove(r)
            else:
                print(data)
