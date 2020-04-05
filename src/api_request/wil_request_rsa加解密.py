# -*- coding: utf-8 -*-
"""
@time: 2020/3/1 20:56
@author: pei.lu
"""
# import jpype
import os
# pip install jpype1==0.7.0
# 如何在python中调用jar库
class enCrypt:
    def __init__(self):
        jdkpath=os.environ['JAVA_HOME']
        print(jdkpath)  # C:\Program Files\Java\jdk1.8.0_101
        # 用jvm来跑jar库
        jpype.startJVM(jdkpath+r'\jre\bin\server\jvm.dll','-ea',"-Djava.class.path="+'../lib/decript.jar',convertString=False)
        # 获取jar里面要用的java类
        self.jclass=jpype.JClass("com.testingedu.will.Encrypt")
        # 创建对象
        self.obj=self.jclass('../lib/certificate.jks')
    # 加密
    def encrype(self,s):
        jiamistr=str(self.obj.enCrypt(s))
        return jiamistr
    # 解密
    def decrype(self,s):
        jiemistr=str(self.obj.deCrypt(s))
        return jiemistr

import requests,json
en=enCrypt()
# 创建会话，统一管理header，不用login、logout都添加header了
session=requests.session()
result=session.post("http://..../auth")
print(result.text)
jsonres=json.loads(result.text)
session.headers['token']=jsonres['token']
# 登录
en=enCrypt()
res=session.post(".../login",data={'username':'will','password':en.encrypt('123456')})
# 注销
result=session.post(".../logout")
print(result)
