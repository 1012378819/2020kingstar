# -*- coding: utf-8 -*-
"""
@time: 2020/2/21 13:43
@author: pei.lu
"""
# getattr() 获取对象属性值
# 说明：1. 函数功能是从对象object中获取名称为name的属性，等效与调用object.name
# 2. 函数第三个参数default为可选参数，如果object中含义name属性，则返回name属性的值，如果没有name属性，则返回default值，如果default未传入值，则报错。
# hasattr() 检查对象是否含有属性
# setattr() 设置对象的属性值
# delattr() 删除对象的属性

# 定义类Student
class Student:
    def __init__(self, name):
        self.name = name
    def set(self,a,b):
        a,b=b,a
        print(a,b)

s = Student('Aim')
print(hasattr(s,'name'),hasattr(s,'age'))
print(getattr(s, 'name'))  # 等效于调用s.name
print(s.name)
print(getattr(s,'age',6)) # 不存在属性age，但提供了默认值，返回默认值
# print(getattr(s,'age') ) # 不存在属性age，未提供默认值，调用报错
c=getattr(s,'set')
c(3,10)
print(s.__dict__)
setattr(s,'age','18')
s.hobby='piano'
print(s.__dict__)
delattr(s,'hobby')
print(s.__dict__)

# python中的反射/自省的实现，是通过hasattr、getattr、setattr、delattr四个内置函数实现的，其实这四个内置函数不只可以用在类和对象中，也可以用在模块等其他地方，只是在类和对象中用的很多，所以单独提出来进行解释。
# hasattr(key)返回的是一个bool值，判断某个成员或者属性在不在类或者对象中
# getattr(key,default=xxx)获取类或者对象的成员或属性，如果不存在，则会抛出AttributeError异常,如果定义了default那么当没有属性的时候会返回默认值。
# setattr(key,value)假如有这个属性，那么更新这个属性，如果没有就添加这个属性并赋值value
# delattr(key)删除某个属性

# 下面是一个反射 / 自省用在模块级别的例子：
import s2
operation = input("请输入URL:")
if operation in s2.__dict__:
    getattr(s2, operation)()
else:
    print("404")

# 模块s2中的代码：
def f1():
    print("首页")

def f2():
    print("新闻")

def f3():
    print("精选")

# 请输入URL: f1
# 首页