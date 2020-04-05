# -*- coding: utf-8 -*-
"""
@time: 2020/3/6 17:00
@author: pei.lu
"""
from socket import *  # 导入套接字

tcp = socket(AF_INET, SOCK_STREAM)  # 创建tcp套接字

tcp.bind(('', 8800))  # 绑定ip,和端口，客户端需要连接这个ip和端口进行服务器连接。

tcp.listen(5)  # tcp监听，参数为可连接的数量。

newsocket, addr = tcp.accept()  # 接收客户端的连接，并返回一个新的socket和客户端地址。阻塞程序等待客户端的接入。

while 1:  # 表示while True,只要条件类型不是空类型、0和None的False类型则就表示while True。
    socketDate = newsocket.recv(1024)  # 接收客户端的数据。
    if len(socketDate) > 0:  # 如果接收数据的长度大于0，则打印出接收到的信息，如果接收的数据长度为0，则表示客户端使用close方法关闭了套接字。
        print(socketDate.decode('utf-8'))  # 将接收数据解码为utf-8输出
    else:  # 如果客户端关闭了套接字，则跳出循环
        break

    sendDate = input('请输入要回复的内容：')  # 输入需要回复的数据
    newsocket.send(sendDate.encode('utf-8'))  # 使用send将数据编码为utf-8回复

newsocket.close()  # 关闭与客户端通信的套接字。
tcp.close()  # 关闭服务器的套接字，关闭后将不会再接收客户端的连接。