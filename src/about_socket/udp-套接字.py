# -*- coding: utf-8 -*-
"""
@time: 2020/3/6 16:52
@author: pei.lu
"""
# socket套接字是用来在网络间通信的模块。
from socket import *
from threading import *

udp=socket(AF_INET,SOCK_DGRAM) # 创建套接字,基于UDP传输协议。相对于TCP比较快。AF_INET表示使用IPV4进行链接。如果使用IPV6则把参数修改为AF_INET6
udp.bind(('',8080)) #绑定任意ip,和8080端口，如果不进行绑定，那么每创建一个套解字就会使用一个动态端口
sendip=input('输入接收方的ip：')
sendport=int(input('输入接收方的端口：'))

def sendinfo(): # 定义发送函数
    while True:
        senddata=input('输入发送内容：')
        udp.sendto(senddata.encode('utf-8'),(sendip,sendport))

def receiveinfo(): # 定义接收函数
    while True:
        recvdata = udp.recvfrom(1024)  # 调用recvfrom方法进行数据接收，并且以元祖的方式返回，第一个参数是数据，第二个参数为IP和端口。与发送格式一致。
        print(recvdata[1], recvdata[0].decode('utf-8'))  # 将接收到的数据进行打印，并将数据进行解码。

def main():
    ts=Thread(target=sendinfo)
    tr=Thread(target=receiveinfo)
    ts.start()
    tr.start()
    ts.join()
    tr.join()

if __name__ == '__main__':
    main()
