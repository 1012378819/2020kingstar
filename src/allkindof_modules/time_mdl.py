# -*- coding: utf-8 -*-
"""
@time: 2020/2/27 8:52
@author: pei.lu
"""
def testTime():
    import time
    print(time.asctime())
    print(time.localtime())
    print(time.strftime('%Y%m%d', time.localtime()))
# testTime()

import datetime
x=datetime.datetime.today()
# y=datetime.datetime(2018,2,28)
print(x)
y=x-datetime.timedelta(days=7)
print(y)
print(y.strftime("%Y%m%d"))
# print(time.strftime('%Y%m%d',y))
# 20190301

import os,time
# os模块的stat()类是用来获取文件属性的常用手段。
fn = r'D:\CSDN\Column\http_server\server_Polar.py'
info=os.stat(fn)
# 分别对应文件大小（字节数）、文件创建时间、修改时间、最后访问实际的时间戳
print(info.st_size,info.st_ctime,info.st_mtime,info.st_atime)
# 时间戳转为习惯表达年月日时分秒的时间格式
print(time.strftime("%Y-%m-%d %X",time.localtime(info.st_ctime))) # '2019-12-06 09:07:57'