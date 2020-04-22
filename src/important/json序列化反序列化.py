# -*- coding:utf-8 -*-
# @Time : 2020/4/8 8:16
# @Author: lup
__author__ = 'pei.lu'

import json

def test_dumps():
    """
    序列化操作
    """
    list = [1,2,3,4,5]
    print('before',type(list))
    list_str = json.dumps(list)
    print('after',type(list_str), list_str,)

    dict = {'username':'xiaoming','age':10}
    print('before',type(dict))
    dict_str = json.dumps(dict)
    print('after',type(dict_str),dict_str)


    tuple = (1,2,3,4)
    print('before',type(tuple))
    tuple_str = json.dumps(tuple)
    print('after',type(tuple_str),tuple_str) #[1,2,3,4]

# test_dumps()

def test_loads():
    """
    反序列化
    """
    list_str = '[1,2,3,4,5,6]'
    list = json.loads(list_str)
    print('list:',type(list),list)

    tuple_0 = ("5","4","3","2","1")
    tuple_str = json.dumps(tuple_0)
    tuple = json.loads(tuple_str)
    print('after tuple:',type(tuple),tuple) #元组序列化之后返回列表类型

# test_loads()

import requests
import json

# 序列化Json数据并存储到文件中
def test_dump():
    """
    json.dump 将json数据 存入到文件中
    :return:
    """
    r = requests.get(url='http://39.107.96.138:3000/api/v1/topics')
    # dump
    json.dumps(r.json(),open('data.json',mode='w+'))


#data.json
# {
#   "success": true,
#   "data": [
#     {
#       "id": "5e66e7c31a33065b8763dc0d",
#       "author_id": "5d67af5c692231084ca27cd0",
#       "tab": "share",
#       "create_at": "2020-03-10T01:05:07.410Z",
#       "author": {
#         "loginname": "user8",
#         "avatar_url": "//gravatar.com/avatar/d6e3a97ea77c3cc3fe9493150f349088?size=48"
#       }
#     }
#   ]
# }

# 读取data.json数据并转换为python格式

def test_load():
    data = open('./data.json',mode='r',encoding='utf8')
    d = json.load(data)
    print('d:',type(d),d)