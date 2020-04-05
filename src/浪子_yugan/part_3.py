import math
class Friend():
    def __init__(self):
        self.name='wangsna'
        self.gender='female'
    def printA(self):
        print(self.name)
    def set_age(self):
        self.age=20
    def get_age(self):
        return self.age
    
f=Friend()
print(f.__dict__)
print(Friend.__dict__)
f.message='hello world' # 动态的添加一个属性
f.fun=lambda x:x**2 # 实例属性为一个函数
print(f.__dict__)
print(Friend.__dict__)
print(object.__dict__)
print(f.name,f.message,f.fun,f.fun(4),sep='\n')
print(__name__)
# print(f.get_age())  报错，因为还没有设置age属性
f.set_age()
print(f.get_age())

""" 参数格式化输出 """
#%d十进制，%x 十六进制，%o八进制
#%s字符串
#%f浮点数
#%r将后面给的参数原样打印
def testprint():
    num=0x20
    print("the length of %s is %d" %("abcdefg",len("abcdefg")))
    print("%x,%d" %(num,num))
    print("%f,%10.3f,%-10.3f" %(math.pi,math.pi,math.pi))
    print("%r %r %r %r" %(1,-1.677,'fsfs',True))
    #format使用
    print(format(10.5,'.5f'))
    print(format(10,'5d'))
    a = "Hello world"
    print(a.rjust(20, '*'))
    print(a.ljust(20))  # 输出总长度=a+加占位符，默认为空格
    print(a.center(20, '*'))


testprint()
print("===============")
# Exec与Eval语句的主要区别是，Exec处理字符串里面的代码，而Eval是处理字符串里面的表达式。
def test_exec_eval():
    exec("print('helloworld!')") # exec语句用来执行储存在字符串或文件中的Python语句
    print(eval('2*3')) # eval语句用来计算存储在字符串中的有效Python表达式
    print('2*3')

# test_exec_eval()
def sentence():
    #false,none,0,"",{},[],()被认为是布尔表达式的假
    print(bool([]))
    print(bool(None))
    print(bool('None'))
    # a if b else c ,如果b为真，返回a，否则返回c。不需要引入临时变量，可以直接使用
    y="Y" if 1==1 else "F"
    print(y)
    name=input("please input your name:") or "unknown"  #input返回值为真，就赋给name，否则将默认值unknown返回给name
    print(name)
    #断言
    age=20
    assert 10<age<100
    assert age==10,'the age not in scope'   #条件后加字符串用来解释断言  #AssertionError: the age not in scope

# sentence()

x=1
y=math.sqrt
# print(callable(x),type(x))
# print(callable(y),type(y))
# print(y(16))

#全局变量global
x=1
y='world'
z='hi'

def f():
    global x,z
    y='hello'
    x+=1
    print(x,z)
    print(z+y+globals()['y']) #重名需要用globals()['paramter']获取全局变量

print(x,z)
print(f)
print(f()) # 没有返回值，等于None

# 函数式编程的一个特点就是，允许把函数本身作为参数传入另一个函数，还允许返回一个函数！

# 如果一个变量指向了一个函数，那么，可通过该变量来调用这个函数
f=abs
print(f(-10))

def add(x,y,f):
    print (f(x)+f(y))

add(-5,6,abs)

print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True))
# ['Zoo', 'Credit', 'bob', 'about']
print(sorted([36, 5, -12, 9, -21], key=abs)) 
# [5, 9, -12, -21, 36]

print(dir('abc')) # 获得一个str对象的所有属性和方法
#['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__',
#  '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__',
# '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__',
# '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith',
# 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier',
#  'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition',
#  'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase',
#  'title', 'translate', 'upper', 'zfill']

print(str.__dict__) 
# 实际上，在len()函数内部，它自动去调用该对象的__len__()方法，所以，下面的代码是等价的：
# print(len('ABC')) # 3
# prnit('ABC'.__len__()) # 3
# 我们自己写的类，如果也想用len(myObj)的话，就自己写一个__len__()方法：
#
# >>> class MyDog(object):
# ...     def __len__(self):
# ...         return 100
# ...
# >>> dog = MyDog()
# >>> len(dog)
# 100

"""enumerate使用"""
name=['Lust','Alice','David','Irene']
print(list(enumerate(name)))
for i in range(len(name)):
    print(i+1,name[i])
for i,n in enumerate(name):
    print(i+1,n)

