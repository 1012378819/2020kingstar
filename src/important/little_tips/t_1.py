# -*- coding: utf-8 -*-
"""
@time: 2020/2/21 15:25
@author: pei.lu
"""
# 数值相关内容
print(round(3.456,2))  # 3.46
print(round(3.456,1)) # 3.5
print(round(3.456,0)) # 3.0
print(round(3.456))  # 3 不传入参数，结果四舍五入取整
a1=3.0
print(a1.is_integer())  # True
a1=3.14
print(a1.is_integer())  # False

# 比较相关内容
print((1,2) < (2,3)) # True # 序列比较大小
print(1==1.0) # True 整数类型和浮点数类型间的对象相等比较时，如果两个对象的数值相同，则结果相等

# 自定义类如果实现了__eq__()方法，则可进行相等比较，相等比较结果是__eq__()方法执行返回的结果；
# 不等比较的结果则优先看自定义是否实现了__ne__()方法，如果有实现则不等比较结果是__ne__()方法执行返回的结果，否则是相等比较结果取反后的值
# 类似的，自定义类实现__lt __（），__le __（），__gt __（）和__ge __（）相关方法

# 实现__eq__
class Man():
    def __init__(self,name):
        self.name = name
    def __eq__(self,other):
        return self.name == other.name

a = Man('xiaoming')
b = Man('xiaoming')
print(a == b) # 实现了__eq__方法 True
print(a != b) # 未实现了__ne__方法，是相等比较结果的取反后结果 False