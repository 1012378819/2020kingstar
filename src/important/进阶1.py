# -*- coding:utf-8 -*-
'''
Created on 2020年1月7日

@author: pei.lu
'''
import collections

content=collections.OrderedDict() # 有序字典，可记住键值对的添加顺序
content['name']='zhangsan'
content['age']=20
content['male']='yes'
content['hobby']='piano'
print(content)
print(type(content))


# https://blog.csdn.net/qq_41853758/article/details/82853811
# 闭包
def num(num):  # 定义函数
    def num_in(nim_in):  # 定义函数
        return num + num_in  # 返回两个参数的和。
    return num_in  # 返回内部函数的引用。（变量名）

a = num(100)  # 将参数为100的函数num接收，并赋值给a，只不过这个返回值是一个函数的引用。等于 a = num_in，注意这里接收的不光是函数本身，还有已经传递的参数。
b = a(100)  # 调用函数a,即num_in，并传递一个参数100，返回值给b。

# 装饰器

# 1.装饰没有参数的函数
def function(func):  # 定义了一个闭包
    def func_in():  # 闭包内的函数
        print('这里是需要装饰的内容，就是需要添加的内容')
        func()  # 调用实参函数。
    return func_in

def test():  # 需要被装饰修改的函数。
    print('无参函数的测试')

test = function(test)  # 装饰器的原理就是将原有的函数名重新定义为以原函数为参数的闭包。
test() #这里再次掉用test()的时候，其实是将会调用闭包内的函数func_in()。所以将会起到装饰修改的作用，最后会再次调用原函数test()。

@function  # 装饰器的python写法，等价于test = function(test)，并且无需调用当代码运行道这里，Python会自动运行。
def test():
    print('无参函数的测试')

test()  # 这里再次调用函数时，将会产生修改后的效果。

# 2、装饰带有参数的函数
def function(func):  # 定义了一个闭包
    def func_in(*args, **kwargs):  # 闭包内的函数，因为装饰器运行的实则是闭包内的函数，所以这里将需要有形参用来接收原函数的参数。
        print('这里是需要装饰的内容，就是需要添加的内容')
        func(*args, **kwargs)  # 调用实参函数，并传入一致的实参。
    return func_in

@function  # 装饰器的python写法，等价于test = function(test) .
def test():
    print('无参函数的测试')

test(5,6)  # 这里再次掉用test()的时候，其实是将会调用闭包内的函数func_in()。所以将会起到装饰修改的作用，最后会再次调用原函数test()。

# 3、装饰带有返回值的函数

def function(func): #定义了一个闭包
	def func_in(*args,**kwargs): #闭包内的函数，因为装饰器运行的实则是闭包内的函数，所以这里将需要有形参用来接收原函数的参数。
		print('这里是需要装饰的内容，就是需要添加的内容')
		num = func(*args,**kwargs) #调用实参函数，并传入一致的实参，并且用变量来接收原函数的返回值，
		return num #将接受到的返回值再次返回到新的test()函数中。
	return func_in
@function
def test(a,b): #定义一个函数
	return a+b #返回实参的和

# 4、带有参数的装饰器
def func(*args, **kwags):
    def function(func):  # 定义了一个闭包
        def func_in(*args, **kwargs):  # 闭包内的函数，因为装饰器运行的实则是闭包内的函数，所以这里将需要有形参用来接收原函数的参数。
            print('这里是需要装饰的内容，就是需要添加的内容')
            num = func(*args, **kwargs)  # 调用实参函数，并传入一致的实参，并且用变量来接收原函数的返回值，
            return num  # 将接受到的返回值再次返回到新的test()函数中。
        return func_in
    return function

@func(50)  # 这里会先运行函数func，并切传入参数，之后会再次运行闭包函数进行装饰, @func(50)>>@function，然后将由@function继续进行装饰修改。
def test(a, b):
    print('这是一个函数')
    return a+b

class Test(object):  # 定义一个类
    def __init__(self,func):
        self.__func = func

def __call__(self):  # 定义call方法，当直接调用类的时候，运行这里。
    print('这里是装饰的功能')
    self.__func()

t = Test()  # 实例化对象
t()  # 调用类，将会调用call方法。

@Test  # 类装饰器等于test = Test(test),将函数test当作参数传入类中的init方法，并将函数名赋值给私有属性__func，当函数test被调用的时候，其实是运行Test类中的call方法.
def test():
    print('被装饰的函数')
test()  # 这里调用的不在是函数test，而是实例对象test的call方法，会先进行装饰，然后再调用私有属性__func(),__func 其实就是被装饰的函数test。

print("==============================")

# 动态语言添加属性和方法
class Person():  # 创建一个类
    def __init__(self, name):  # 定义初始化信息。
        self.name = name

li = Person('李')  # 实例化Person('李'),给变量li
li.age = 20  # 再程序没有停止下，将实例属性age传入。动态语言的特点。
Person.age = None  # 这里使用类名来创建一个属性age给类，默认值是None。Python支持的动态属性添加。

def eat(self):  # 定义一个方法，不过这个方法再类之外。
    print('%s正在吃东西。。' % self.name)

import types  # 动态添加方法需要使用tpyes模块。

li.eat = types.MethodType(eat, li)  # 使用types.MethodType，将函数名和实例对象传入，进行方法绑定。并且将结果返回给li.eat变量。实则是使用一个和li.eat方法一样的变量名用来调用。
li.eat()  # 调用外部方法eat()方法。

@staticmethod  # 定义静态方法。
def test():  # 定义静态方法，静态方法可以不用self参数。
    print('这是一个静态方法。')

Person.test = test  # 使用类名.方法名 = test的形式来方便记忆和使用，Person.test其实只是一个变量名，没有特殊的含义。
Person.test()  # 调用test方法。

@classmethod  # 类方法
def test(cls):
    print('这是一个类方法。')

Person.test = test  # 定义一个类属性等于方法名。
Person.test()  # 调用方法。

class test(object):  # 定义一个类。
    __slots__ = ('name', 'age')  # 使用slots来将属性固定，不能进行动态添加修改。





