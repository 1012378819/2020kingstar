# -*- coding:utf-8 -*-
'''
Created on 2019年12月22日

@author: pei.lu
'''
class CapStr(str):
    def __new__(cls,string):
        string=string.upper()
        return str.__new__(cls,string)

a=CapStr("this is new knowledge")
print(a)

class C:
    def __init__(self):
        print('我是 构造方法，对我的实例化时，我被执行')
    def __del__(self):
        print('我是 析构方法，对我的引用为0时，我被执行')
        
c1=C()  # 为啥结果会直接输出析构方法？
# c2=c1
# c3=c2

# del c3
# del c2
# del c1

class new_int(int):
    def __add__(self,other):
        return int.__sub__(self,other)  # 实际进行减法
    def __sub__(self,other):
        return int.__add__(self,other)  # 实际进行加法
        
a=new_int(3)
b=new_int(5)
print(a+b)
print(a-b)

print('===============')

def checkIndex(key):
    if not isinstance(key,(int,)):raise TypeError
    if key<0:raise IndexError

class ArithmeticSequence:
    def __init__(self,start=0,step=1):
        self.start=start   # 保存开始值
        self.step=step     # 保存步长
        self.changed={}    # 没有项被修改

    def __getitem__(self, key):  # 返回所给键对应的值
        checkIndex(key)
        try: return self.changed[key]        # 修改了吗？
        except KeyError:                     # 否则。。。
            return self.start+key*self.step  # 。。。计算值

    def __setitem__(self, key, value): # 按一定的方式存储和key相关的value
        checkIndex(key)
        self.changed[key]=value    # 保存更改后的值

s=ArithmeticSequence(1,2)
print(s[4])
s[4]=2
print(s.changed)
print(s[4])
print(s[5])
# print(s["four"]) #TypeError
# print(s[-23]) #IndexError
# del s[4] #AttributeError,没有实现__delitem__方法

class CounterList(list): # 继承list类
    def __init__(self,*args):
        super(CounterList,self).__init__(*args)
        self.counter=0  # 新计数属性
    def __getitem__(self, index):
        self.counter+=1
        return super(CounterList,self).__getitem__(index)

c1=CounterList(range(10))
print(c1)
c1.reverse()
print(c1)
del c1[3:6]
print(c1)
print(c1.counter)
print(c1[4]+c1[2])
print(c1.counter)
