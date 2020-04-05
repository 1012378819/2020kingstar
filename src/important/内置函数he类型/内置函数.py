# -*- coding: utf-8 -*-
"""
@time: 2020/2/21 17:01
@author: pei.lu
"""

c='cccc'
def globals_locals():
    global b
    print(locals())
    a=1
    b=5
    print(locals())
    print(globals()) # c='cccc'也是全局变量

# globals_locals()
pow(2,3,5) # pow(2,3)%5=8%5=3
sum((1,4,7))
sum((1,4,7),10) # sum() sum expected at most 2 arguments
sum([1,4,5])
sum({1,4,5},-22.093)
float() #不提供参数的时候，返回0.0
# ord：返回Unicode字符对应的整数
ord('a') # 97
# chr：返回整数所对应的Unicode字符
chr(97) # 'a'
# bytes：根据传入的参数创建一个新的不可变字节数组
bytes('中文','utf-8') # b'\xe4\xb8\xad\xe6\x96\x87'
# bin：将整数转换成2进制字符串
bin(3) # '0b11'
# oct：将整数转化成8进制数字符串
oct(10) # '0o12'
# hex：将整数转换成16进制字符串
hex(15) # '0xf'
dict(a = 1,b = 2) #  传入键值对创建字典。{'b': 2, 'a': 1}
dict((('a',1),('b',2))) # 传入可迭代对象创建字典。{'b': 2, 'a': 1}
dict(zip(['a','b'],[1,2])) # 传入映射函数创建字典。{'b': 2, 'a': 1}
# frozenset：根据传入的参数创建一个新的不可变集合
a = frozenset(range(10)) # a: frozenset({0, 1, 2, 3, 4, 5, 6, 7, 8, 9})
# enumerate：根据可迭代对象创建枚举对象
list(enumerate(['Spring', 'Summer', 'Fall', 'Winter'], start=1)) # [(1, 'Spring'), (2, 'Summer'), (3, 'Fall'), (4, 'Winter')]

# all：判断可迭代对象的每个元素是否都为True值
all([1,2]) #列表中每个元素逻辑值均为True，返回True
all([0,1,2]) #列表中0的逻辑值为False，返回False
all(()) # 空元组True
all({}) # 空字典True

# any：判断可迭代对象的元素是否有为True值的元素
any([0,1,2]) #列表元素有一个为True，则返回True
any([0,0]) #列表元素全部为False，则返回False
any([]) #空列表False
any({}) #空字典 False

# reversed：反转序列生成新的可迭代对象
# >>> a = reversed(range(10)) # 传入range对象
# >>> a # 类型变成迭代器
# <range_iterator object at 0x035634E8>
# >>> list(a)
# [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

# 返回对象的哈希值，用整数表示。哈希值在字典查找时，可用于快速比较键的值。
hash('good good study')

# eval：执行动态表达式求值
eval('1+2+3+4')  # 10
# exec：执行动态语句块
# >>> exec('a=1+2') #执行语句
# >>> a
# 3

# repr：返回一个对象的字符串表现形式(给解释器)
# 1. 函数功能返回一个对象的字符串表现形式。其功能和str函数比较类似，但是两者也有差异：函数str() 用于将值转化为适于人阅读的形式，而repr() 转化为供解释器读取的形式。
# >>> a = 'some text'
# >>> str(a)
# 'some text'
# >>> repr(a)
# "'some text'"
# 2. repr函数的结果一般能通过eval()求值的方法获取到原对象。
# >>> eval(repr(a))
# 'some text'
# 如果要改变类型的repr函数显示信息，需要在类型中定义__repr__函数进行控制。
class Student:
    def __init__(self,name):
        self.name = name
    def __repr__(self):
        return ('a student named ' + self.name)

# >>> b = Student('Kim')
# >>> repr(b)
# 'a student named Kim'


"""反射操作"""
# __import__  动态导入模块
# 1. 函数功能用于动态的导入模块，主要用于反射或者延迟加载模块。
# 2. __import__(module)相当于import module
# 3. __import__(package.module,fromlist)相当于from package import name，如果fromlist不传入值，则返回package对应的模块，如果fromlist传入值，则返回package.module对应的模块。

# isinstance：判断对象是否是类或者类型元组中任意类元素的实例
isinstance(1,(int,str)) # True
# issubclass：判断类是否是另外一个类或者类型元组中任意类元素的子类
issubclass(bool,(str,int)) # True
issubclass(bool,(int)) # True

# callable：检测对象是否可被调用,可被调用指的是对象能否使用()括号的方法调用。
# 2. 可调用对象，在实际调用也可能调用失败；但是不可调用对象，调用肯定不成功。
# 3. 类对象都是可被调用对象，类的实例对象是否可调用对象，取决于类是否定义了__call__方法
callable(1) # False
# class A:  # 定义类A
#     pass
#
# >>> callable(A)  # 类A是可调用对象
# True
# >>> a = A()  # 调用类A
# >>> callable(a)  # 实例a不可调用
# False
#
# class B:  # 定义类B
#     def __call__(self):
#         print('instances are callable now.')

# >>> callable(B)  # 类B是可调用对象
# True
# >>> b = B()  # 调用类B
# >>> callable(b)  # 实例b是可调用对象
# True
# >>> b()  # 调用实例b成功
# instances are callable now.

#装饰器
# staticmethod函数是将一个方法定义成类的静态方法，使用 @staticmethod装饰器，这样在实例对象调用的时候，不会把实例对象本身传入静态方法的第一个参数了。
class Student(object):
    def __init__(self,name):
        self.name = name
    @staticmethod
    def sayHello(lang):
        print(lang)
        if lang == 'en':
            print('Welcome!')
        else:
            print('你好！')
    def sayHello_2(lang):
        print(lang)
        if lang == 'en':
            print('Welcome!')
        else:
            print('你好！')
Student.sayHello('en')
S=Student('d')
S.sayHello('dd')
S.sayHello_2()