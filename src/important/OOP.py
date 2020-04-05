# -*- coding: utf-8 -*-
#@time: 2019/12/5 10:52
#@author: pei.lu
# from traceback import print_stack
class A:
    def __init__(self, a, b, c):
        self.a = 10      # 公有
        self._b = b      # 保护
        self.__c = c     # 私有

    def getA(self):      # 公有
        return self.a

    def setA(self, a):   # 公有
        self.a = a

    def getB(self):      # 公有
        return self._b

    def _setB(self, b):  # 保护
        self._b = b

    def getC(self):      # 公有
        return self.__c

    def __setC(self, c): # 私有
        self.__c = c

a = A(10, 20, 30)
class B(A):
    pass
b = B(10, 20, 30)
## 试试访问公有成员：
print(a.a) # 10
print(a.getA()) # 10
a.setA(5)
print(a.a) # 5
print(b.a) # 10
print(b.getA()) # 10
b.setA(8)
print(b.a) # 8

## 看看私有成员：
# print(a.__c) # 报错
# print(b.__c) # 报错
print(a.getC()) # 30
print(b.getC()) # 30
# a.__setC(5) # 报错
# b.__setC(5) # 报错

## 在 Python 的OOP中，保护成员公有成员没有任何区别。保护规则仅适用于 from xxx import * 这一种情况。

# 如果要让内部属性不被外部访问，可以把属性的名称前加上两个下划线__，在Python中，实例的变量名如果以__开头，就变成了一个私有变量
# 只有内部可以访问，外部不能访问
# 在Python中，变量名类似__xxx__的，也就是以双下划线开头，并且以双下划线结尾的，是特殊变量，特殊变量是可以直接访问的，
# 不是private变量， 不能用__name__、__score__这样的变量名。
# 有些时候，你会看到以一个下划线开头的实例变量名，比如_name，这样的实例变量外部是可以访问的，但是，按照约定俗成的规定，当你看到这样的变量时，
# 意思就是，“虽然我可以被访问，但是，请把我视为私有变量，不要随意访问”。
print('================')
class Person():
    members=0
    def __init__(self, name, score):
        self.__name = name
        self.score = score
    def __A(self):
        print("something you can't see")
    def B(self):
        print("i am normal method")
        self.__A()
    def init(self):
        Person.members+=1
    def print_score(self):
        print('%s: %s' % (self.__name, self.score))
    
p = Person('lily', 55)
print(p.score)
# print(p.__name) # 报错
print(p._Person__name) 
p.B()
#p.__A()  #方法命名前加双下划线为私有方法，不能在类外访问；所以会报错
p._Person__A() #可以使用这种单下划线加类名的形式去访问私有方法，不常用
p.print_score()

a1=Person('lucy',12)
a2=Person('jack',32)
a1.init()
print("a1init执行完后，类属性值",Person.members)
a2.init()
print("a2init执行完后，类属性值",Person.members)

print('a1.memers=',a1.members) #实例访问类属性
print('a2.memers=',a2.members)

a1.members='new value'  #改变实例属性，类似局部变量把全局变量屏蔽
print('a1.memers=',a1.members) #实例访问类属性,
print('a2.memers=',a2.members)




