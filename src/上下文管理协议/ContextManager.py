# -*- coding:utf-8 -*-
'''
Created on 2019年12月20日

@author: pei.lu
'''
# with语句的本质：上下文管理协议
with open('a.txt',encoding='UTF-8') as f:
    print(f.read())
    
