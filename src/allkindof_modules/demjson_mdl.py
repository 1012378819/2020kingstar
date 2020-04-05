# -*- coding: utf-8 -*-
"""
@time: 2020/2/26 16:59
@author: pei.lu
"""
import json
# python中的json对象，其实就是字典类型。
# 利用json模块，可以将字符串类型的json串转换为 json对象（字典对象），也可以将json对象（字典对象）转换为字符串对象。
# json.dumps() 编码，字典转成字符串
# json.loads() 解码，字符串转成字典
str1='{"job":"teacher","member":{"user":"lp","age":18}}'
obj = json.loads(str1)  # 字符串转字典对象(json对象)
type(obj)  # <type 'dict'>
print(obj)
# 字典层次化显示
obj_c=json.dumps(obj,indent=4)
print('层次化显示结果：\n',obj_c)
value = json.dumps(obj) # 字典对象转字符串
type(value) # <type 'str'>
print('dumps后的值为{}'.format(value))

# 写文件
d={'first':'one','second':2}
json.dump(d,open('a.txt','w'))
#读json
newd=json.load(open('a.txt','r'))
print(d,type(d))

print("=============分割线================")
# python解析非标准格式json--demjson
import demjson
str2dict = '{a : 1,b : 2,c : 3}'
# json.loads(str2dict) # 报错：json.decoder.JSONDecodeError: Expecting property name enclosed in double quotes: line 1 column 2 (char 1)


# demjson主要用法：
# 把dict转换为str
dict2str ={'a':1,'b':3}
print(demjson.encode(dict2str)) # '{"a":1,"b":3}'

# 把str转换为dict
str2dict = '{a : 1,b : 2,c : 3}'
print(demjson.decode(str2dict)) # {'a': 1, 'b': 2, 'c': 3}
