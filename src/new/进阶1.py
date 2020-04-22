# -*- coding:utf-8 -*-
'''
Created on 2020年1月7日

@author: pei.lu
'''

# 动态语言添加属性和方法
class Person():  # 创建一个类
    def __init__(self, name):  # 定义初始化信息。
        self.name = name

li = Person('李')  # 实例化Person('李'),给变量li
li.age = 20  # 再程序没有停止下，将实例属性age传入。动态语言的特点。
Person.age = None  # 这里使用类名来创建一个属性age给类，默认值是None。Python支持的动态属性添加。


print(Person('li'))
print(li)
print(Person.age)
print(li.age)

def eat(self):  # 定义一个方法，不过这个方法在类之外。
    print('%s正在吃东西。。' % self.name)

import types  # 动态添加方法需要使用types模块。
li.eat = types.MethodType(eat, li)  # 使用types.MethodType，将函数名和实例对象传入，进行方法绑定。并且将结果返回给li.eat变量。实则是使用一个和li.eat方法一样的变量名用来调用。
li.eat()  # 调用外部方法eat()方法。

@staticmethod  # 定义静态方法。
def test():  # 定义静态方法，静态方法可以不用self参数。
    print('这是一个静态方法。')

Person.test = test  # 使用类名.方法名 = test的形式来方便记忆和使用，Person.test其实只是一个变量名，没有特殊的含义。
Person.test()  # 调用test方法。
li.test()

@classmethod  # 类方法
def test(cls):
    print('这是一个类方法。')

Person.test = test  # 定义一个类属性等于方法名。
Person.test()  # 调用方法。
li.test()

class NewTest(object):  # 定义一个类。
    __slots__ = ('name', 'age')  # 使用slots来将属性固定，不能进行动态添加修改。

A=NewTest()
A.name='k'
# A.newslot='k' #报错，不能添加

# ---------------------------------
# __new__ 单例模式学习

class Dog:
    def __init__(self):
        print('init方法执行')
    def __str__(self):
        print('str方法执行')
        return '对象描述信息'
    def __del__(self):
        print('del方法执行')

    def __new__(cls, *args, **kwargs):#cls 是Dog指向的类对象
        print(id(cls))
        print('new方法执行')
        return object.__new__(cls)

print(id(Dog))
xtq = Dog()
# 1.调用new方法创建对象，找一个变量来接收new 的返回值，这个返回值表示创建出来对象的引用
# 2.__inin__（刚刚创建出的对象的引用）
# 3.返回对象的引用

class PositiveInt(int):
    def __new__(cls,value):
        super(PositiveInt,cls).__new__(cls,abs(value))

x=PositiveInt(-3)
print(x)



# 因为类每一次实例化后产生的过程都是通过__new__来控制的，所有通过重载__new__方法，我们可以很简单的实现单例模式
class Singleton:
    instance = None
    def __new__(cls, xx, yy):
        if cls.instance is None:
            cls.instance = super().__new__(cls)
        return cls.instance

    def __init__(self, xx, yy):
        self.xx = xx
        self.yy = yy

obj1 = Singleton(1, 2)
print(obj1.xx, obj1.yy)
obj2 = Singleton(3, 4)

print(obj1.xx, obj1.yy)
print(obj2.xx, obj2.yy)
print(obj1 is obj2)

