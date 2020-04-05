# -*- coding: utf-8 -*-
"""
@time: 2020/3/6 17:00
@author: pei.lu
"""
from socket import *  # 导入模块

csocket = socket(AF_INET, SOCK_STREAM)  # 创建套接字

serverIp = input('请输入服务器的IP:')

csocket.connect((serverIp, 8800))  # 连接服务器

while 1:
    sendData = input('请输入需要发送打内容:')  # 输入发送的内容
    csocket.send(sendData.encode('utf-8'))  # 编码发送

    recvData = csocket.recv(1024)
    print('recvData:%s' % recvData.decode('utf-8'))  # 解码输出

csocket.close()  # 关闭套接字