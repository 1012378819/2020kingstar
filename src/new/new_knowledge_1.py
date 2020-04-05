# -*- coding: utf-8 -*-
#@time: 2020/1/12 21:32
#@author: pei.lu
# 利用 sys.getsizeof() 来检查对象使用内存的状况
import sys

def test_ram():
    my_list=range(0,10000)
    print(sys.getsizeof(my_list))
    my_real_list=[x for x in range(0,10000)]
    print(sys.getsizeof(my_real_list))

# test_ram()
""" 
# list.sort()和sorted()都是python的内置函数，他们都用来对序列进行排序，区别:
# list.sort()是对列表就地(in-place)排序，返回None；sorted()返回排好序的新列表，原列表不变
# sort()只适用于列表，sorted()适用于任意可迭代对象
# sort 是应用在 list 上的方法，sorted 可以对所有可迭代的对象进行排序操作
"""
def test_sort():
    l=[1,4,-5.11,12.1,66.22,0]
    l2=l[:]
    print('最大值：',max(l),'最小值：',min(l))
    return_l=l.sort()
    print('排序后l：',l,return_l)  # 返回None，直接改变的是list
    return_l2=sorted(l2)
    print('排序后l2：', l2,return_l2) # 返回排序的新list，原list不变
    my_dict = {"a": "1", "c": "3", "b": "2"}
    print('字典排序：',sorted(my_dict)) # 对dict排序默认会按照dict的key值进行排序，最后返回的结果是一个对key值排序好的list

# test_sort()

def test_sort_with_key():
    # 当列表由list（或者tuple）组成时，默认情况下，sort和sorted都会根据list[0]（或者tuple[0]）作为排序的key，进行排序。
    L=[(8, 'Logan', 20), (2, 'Mike', 22), (5, 'Lucy', 19)]
    print(sorted(L))
    print(sorted(L,key=lambda x:x[2]))
    print(sorted(L, key=len))
    my_dict = {"a":"2", "c":"5", "b":"1"}
    print('字典按value排序结果：',sorted(my_dict,key=lambda x:my_dict[x])) # 按字典的value排序，返回值还是key组成的list

# test_sort_with_key()

def test_sort_with_reverse():
    l = [1, 4, -5.11, 12.1, 66.22, 0]
    print(sorted(l))
    print(sorted(l,reverse=True))

# test_sort_with_reverse()

#
# 判断字典中是否已包含某key
# python2  dict.has_keys('key')
# python3  dict.get('key')   没有的话返回None

from collections import Counter
print(Counter(['a','b','a','d','aa','b','a'])) # 返回字典，值为迭代对象的元素计数
print(Counter('abcdabcaba')) # 返回字典，值为迭代对象的元素计数
d=Counter('hello world')
print(d.most_common(2)) # [('1',3),('0',2)]

students=['Peter','Tom','Jack']
grades=[90,80,89]
print(zip(students,grades))
print(list(zip(students,grades)))  # [('Peter', 90), ('Tom', 80), ('Jack', 89)]
print(dict(zip(students,grades)))  # {'Peter': 90, 'Tom': 80, 'Jack': 89}

def a():
    return [1,2][1<10] # 后一个条件正确返回2，错误返回1
# print(a())

import re
s="i love python"
s1="i /..love >?python"
x1=s.split()
x2=re.split('\W+',s1) # 去除字符串中不需要的字符然后split
x3=re.split('\w+',s1)
print(x1,x2,x3)

# 列表的展开
a=[[1,4],['d','b'],{3,1},(4,88),{'name':'lp','age':16}]
print([x for i in a for x in i])

# max函数
dict_1={'a':5,'b':10,'c':6}
print(max(dict_1,key=lambda x:dict_1[x]))

# 数字字符串转为数字列表
a='1234765'
print([int(i) for i in a]) # 实现1
print(list(map(int,a)))   # 实现2

#  object类没有定义 __dict__，所以不能对object类实例对象尝试设置属性值。
# >>> a = object()
# >>> a.name = 'kim' # 不能设置属性
# Traceback (most recent call last):
#   File "<pyshell#9>", line 1, in <module>
#     a.name = 'kim'
# AttributeError: 'object' object has no attribute 'name'
#
# #定义一个类A
# >>> class A:
#     pass
#
# >>> a = A()
# >>>
# >>> a.name = 'kim' # 能设置属性

# vars：返回当前作用域内的局部变量和其值组成的字典，或者返回对象的属性列表
#作用于类实例
# >>> class A(object):
#     pass
# >>> a.__dict__
# {}
# >>> vars(a)
# {}
# >>> a.name = 'Kim'
# >>> a.__dict__
# {'name': 'Kim'}
# >>> vars(a)
# {'name': 'Kim'}

# 两个模块都有同一个函数，导入的时候可以用as提供别名
# from moduleA import func as func1
# from moduleA import func as func2

print(sorted([32,5,12,8,1])) # sorted方法返回列表
print(list(reversed('helloworld'))) # reversed（反转）返回可迭代对象
print({ x:x%2==1 for x in range(1,8)}) # 生成字典
from math import sqrt
for n in range(99,81,-1): # while else同for else 正常退出时（非break，continue，ctrl+C），执行else
    root=sqrt(n)
    if root==int(root):
        print(n)
        break  #当循环没有调用break时执行else
else:  # 非正常退出（如：ctrl+c、break、continue）：不执行else
    print('not find it')

# and和or是逻辑运算符号，返回值不一定是Bool类型，而是参与运算的某个量的类型
# and返回参与运算的量中第一个False的值，如果没有，返回最后一个量
# or返回参与运算的量中第一个True的值，如果没有，返回最后一个量
# >>> 3 and 4 # 4
# >>> 3 and 0 and 4 # 0
# >>> 5 or 6 # 5
# >>> 0 or 6 # 6
# >>> 0 or 0 # 0
# >>> 3 and 4*5 or 6 # 20
