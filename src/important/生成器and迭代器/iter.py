#一个实现了__iter__方法的对象是可迭代的，一个实现了__next__方法的对象是迭代器
#迭代器是带有__next__方法的简单对象
class Fibs:
    def __init__(self):
        self.a=0
        self.b=1
    def __next__(self):
        self.a,self.b=self.b,self.a+self.b
        return self.a
    def __iter__(self):
        return self

fibs=Fibs()
for f in fibs:
    if f>1000:  #查找斐波那契数列中比1000大的数中最小的数
        print(f)
        break

it=iter([1,2,3,4,5])
print(next(it))
print(next(it))
print(it.__next__())


# a = iter('abcd') #字符串序列
# >>> next(a)  # 'a'
# >>> next(a)  # 'b'
# >>> next(a)  # 'c'
# >>> next(a)  # 'd'
# >>> next(a)
# Traceback (most recent call last):
#   File "<pyshell#29>", line 1, in <module>
#     next(a)
# StopIteration
#传入default参数后，如果可迭代对象还有元素没有返回，则依次返回其元素值，如果所有元素已经返回，则返回default指定的默认值而不抛出StopIteration 异常
# >>> next(a,'e')   # 'e'

print('=================')
class TestIterator:
    value=0
    def __next__(self):
        self.value+=1
        if self.value>10:
            raise StopIteration
        return self.value
    def __iter__(self):  #去掉的话就报错，提示不可迭代
        return self

t1=TestIterator()
print(list(t1))

def test():
    r = map(lambda x:x*x, [1, 2, 3, 4, 5])
    print('next1:',next(r))
    print('next2:',next(r))
    print(list(r))  # 由于结果r是一个Iterator，Iterator是惰性序列，因此通过list()函数让它把整个序列都计算出来并返回一个list。
    print('结果:',list(map(str, [1, 2, 3, 4, 5])))  # 把list的所有数字转为字符串

test()

""" iterator部分 """
# 可以直接作用于for循环的数据类型有以下几种：
# 一类是集合数据类型，如list、tuple、dict、set、str等；
# 一类是generator，包括生成器和带yield的generator function。
# 这些可以直接作用于for循环的对象统称为可迭代对象：Iterable。
# 可以使用isinstance()判断一个对象是否是Iterable对象

from collections.abc import Iterable,Iterator

# 当我们使用for循环时，只要作用于一个可迭代对象，for可以正常运行，而我们不太关心该对象究竟是list还是其他数据类型。
def test1():
    print(isinstance('abc',Iterable)) #str可迭代
    print(isinstance([],Iterable)) #list可迭代
    print(isinstance((),Iterable)) #tuple可迭代
    print(isinstance(123,Iterable)) #整数不可迭代
# 而生成器不但可以作用于for循环，还可以被next()函数不断调用并返回下一个值，直到最后抛出StopIteration错误表示无法继续返回下一个值了。
# 可以被next()函数调用并不断返回下一个值的对象称为迭代器：Iterator。
# 可以使用isinstance()判断一个对象是否是Iterator对象：
def test2():
    print(isinstance('abc',Iterator)) #str不是迭代器
    print(isinstance(iter('abc'),Iterator)) #变成迭代器
    print(isinstance([],Iterator)) #list不是迭代器
    print(isinstance(iter([]),Iterator))  #变成迭代器
    print(isinstance((),Iterator)) #tuple不是迭代器
    print(isinstance((x for x in range(10)),Iterator)) #是迭代器
print([x for x in range(10)])
print(isinstance([x for x in range(10)],Iterator))
print((x for x in range(10)))
print(isinstance((x for x in range(10)),Iterator))


# 类的对象如果想要变成一个可迭代对象，那么对象中必须要有__iter__方法，并且这个方法返回的是一个迭代器。
# for 循环的对象如果是一个可迭代的对象，那么会先执行对象中的__iter__方法，获取到迭代器，然后再执行迭代器中的__next__方法获取数据。如果for循环的是一个迭代器，那么直接执行迭代器中的__next__方法。
#
# class Foo:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def __iter__(self):
#         return iter([1,2,3,4,5])  # 返回的是一个迭代器
# li=Foo("alex",18)
#
# # 1.如果类中有__iter__方法，他的对象就是可迭代对象
# # 2.对象.__iter()的返回值是一个迭代器
# # 3.for循环的如果是迭代器，直接执行.next方法
# # 4.for循环的如果是可迭代对象，先执行对象.__iter()，获取迭代器再执行next
#
# for i in li:
#     print(i)

