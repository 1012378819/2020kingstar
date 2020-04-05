"""
lambda、map、filter、reduce函数使用,zip函数
"""

# lambda :
#  使用方法: lambda 参数：操作（参数）

# 当我们在传入函数时，有些时候，不需要显式地定义函数，直接传入匿名函数更方便
lambda x:x*x
# 等于
def f(x):
    return x*x

print(list(map(lambda x:x*x,[1,2,3,4,5])))
# 等于
print(list(map(f,[1,2,3,4,5])))

f=lambda x:x*x # 匿名函数也是一个函数对象，也可以把匿名函数赋值给一个变量，再利用变量来调用该函数
print(f) # <function <lambda> at 0x00000000021D33C0>
print(f(5))

def lambda_test1():
    add=lambda x,y:x+y
    print(add(3,5))

def lambda_test2():
    #单个列表排序
    mylist=[(1,5),(10,2),(4,8),(2,1)]
    mylist.sort(key=lambda x:x[0])
    print(mylist)
    mylist.sort(key=lambda x:x[1])
    print("2次排序：{}".format(mylist))

# lambda_test1()
# lambda_test2()

"""
map用法:
 map(function,iterable,...)
 第一个参数function以参数序列中的每个元素调用function函数，返回包含每次function函数返回值的新列表
function：函数
iterable：1个或多个序列
返回值:
  py2.X 返回列表，py3.X 返回迭代器，节省了内存。
"""
def map_test1():
    #计算平方的函数
    def square(x):
        return(x**2)
    print("range(4) in py3: {}".format((range(4))))
    print("range(4)强制转换成 list in py3: {}".format(list(range(4))))
    map0 = map(square, [0, 1, 2, 3])
    map1 = map(square,range(4))
    print("map0:{}\nmap1:{}".format(map0,map1))
    print("map0 强制转换成 list:{}\nmap1 强制转换成 list:{}".format(list(map0),list(map1)))
    map2=map(lambda x:x**2,[0,1,2,3])
    print(list(map2))
    list1=[2,4,6,8,10]
    list2=[1,3,5,7,9]
    map3=map(lambda x,y:x+y,list1,list2)
    print(list(map3))
    def fun(a,b):
        return a*10+b
    map4=map(fun,[1,2],[3,4])
    print('map4:{}'.format(list(map4)))
    print([str(i) for i in range(10)])
    print(list(map(str,range(10)))) # 结果同上
    # map5=map(None,[1,2,'a'],['b',3])
    # print(list(map5)) 'py3报错，py2结果[(1,'b'),(2,3),('a',None)]
# map_test1()

# map()函数接收两个参数，一个是函数，一个是Iterable，map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回。

#把用户名变成首字母大写的名字
def normalize(name):
    name=list(name)
    name[0]=name[0].upper()
    return ''.join(name)

# 测试:
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
L3= list(i.capitalize() for i in L1)
# print(L2)
# print(L3)

"""
filter()
# 用法:filter(function,iterable)
#原理：filter()函数用于过滤序列，筛选出符合条件的元素，返回符合条件元素组成的列表。
# filter()函数接受两个参数，第一个为函数，第二个为序列，序列的每个元素作为参数传递给函数进行判断，返回true的放入新列表
#返回值:
#  py2.X 返回列表，py3.X 返回迭代器
"""
def filter_test():
    filter_list=['dffa','abb','sdf']
    filter1=filter(lambda x:'a' in x,filter_list)
    print(list(filter1))

# filter_test()

# Python内建的filter()函数用于过滤序列。
# filter()也接收一个函数和一个序列。filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素
def is_odd(n):
    return n % 2 == 1

# 注意filter()函数返回的是一个Iterator，也就是一个惰性序列，所以需要用list()函数获得所有结果并返回list。
print(list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15])))
# 结果: [1, 5, 9, 15]

def not_empty(s):
    return s and s.strip()

print(list(filter(not_empty, ['A', '', 'B', None, 'C', '  ']))) # ['A', 'B', 'C']


"""
reduce()
#用法:reduce(function,iterable[,initializer])
# function:函数，有两个参数
# iterable:可迭代对象
# initializer：可选，初始参数
# !!!返回函数的计算结果!!!
# 原理：reduce()函数对参数中的序列进行累计，将一个数据集合（链表、元组等）中的所有数据进行如下操作:
#  用传给reduce中的函数function，先对集合中的第1、2个元素进行操作，得到的结果在于第三个数据用function函数运算。。。
# 在py3中需要from functools import reduce 导入使用
"""

# reduce的用法。reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，
# reduce把结果继续和序列的下一个元素做累积计算，
# 效果就是  reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
from functools import reduce

def add(x,y):
    return x+y

print(reduce(add,[1,3,5,7,9]))

def fn(x,y):
    return x*10+y

print(reduce(fn,[1,3,5,7,9]))

DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

def char2num(s):
    return DIGITS[s]

def str2int(s): #把字符串转化为整数的函数
    return reduce(lambda x, y: x * 10 + y, map(char2num, s))

print(str2int('1736'))
print(int('1736')) # 结果同上

#Python提供的sum()函数可以接受一个list并求和，请编写一个prod()函数，可以接受一个list并利用reduce()求积：
def f2(x,y):
        return x*y
def prod(L):
    return reduce(f2,L)

def prod1(L):    # 结果同上
    def fn1(x,y):
        return x*y
    return reduce(fn1,L)

print('1 + 3 + 5 + 7 =',sum([1,3,5,7]))
print('1 * 3 * 5 * 7 =',prod([1, 3, 5, 7])) 

def reduce_test():
    def func(x,y):
        return x*y
    print(reduce(func,[4,1,2,3]))
    
# reduce_test()

# 利用多线程技术在CPU的多个核上，分任务并行计算[0,10000)区间所有整数的平方和
from functools import reduce
import multiprocessing as mp

def power(x):
    return pow(x,2)

with mp.Pool(processes=4) as mpp:
    print(reduce(lambda a,b:a+b,mpp.map(power,range(10000)),0))


#zip函数
#利用python自带的zip函数可同时对两个列表进行遍历，代码如下：
def zip_test():
    list1 = ['a', 'b', 'c', 'd']
    list2 = ['apple', 'boy', 'cat', 'dog']
    for x, y in zip(list1, list2):
        print(x,'is',y)
    a=['zangsna',1,3,5]
    b=['wangwu',4,6]
    print(zip(a,b)) #<zip object at 0x0000000002ECE848>
    print(list(zip(a,b)))
    print([(a,b) for a,b in zip(a,b)])
    print([{a,b} for a,b in zip(a,b)])

# zip_test()

a=[[1,2],[3,4],[5,6]]
print(zip(*a))
print(list(zip(*a)))  # [(1,3,5),(2,4,6)]



# print(''.join([chr(random.randint(0,128)) for x in range(4)]))

L1 = ['Hello', 'World', 18, 'Apple', None]
L2= [ x.lower() for x in L1 if isinstance(x,str)]
print(L2)


def func(x):
    return x.isalnum()  # 检测字符串是否由字母和数字组成
seq=['f02','?!@','***','sf']

print(list((filter(func,seq))))
print(list((filter(lambda x:x.isalnum(),seq)))) # 结果同上
print([x for x in seq if x.isalnum()]) # 结果同上

