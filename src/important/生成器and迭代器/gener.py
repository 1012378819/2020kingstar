# -*- coding:utf-8 -*-
'''
Created on 2019年12月21日

@author: pei.lu
'''
# 通过列表生成式，我们可以直接创建一个列表,如果列表元素可以按照某种算法推算出来，那我们是否可以在循环的过程中不断推算出后续的元素呢？
# 这样就不必创建完整的list，从而节省大量的空间。这种一边循环一边计算的机制，称为生成器：generator。
# 一种方法：把一个列表生成式的[]改成（）就创建了一个generator ；另一种方法：yield
# 注意：生成器是可迭代对象，迭代器不一定是生成器。并且迭代器无法回取，只能向前取值。
# 注意：一个对象具有 iter 方法的才能称为可迭代对象，使用yield生成的迭代器函数，也有iter方法。凡是没有iter方法的对象不是可迭代对象，凡是没有__next__()方法的不是是生成器。
# python中生成器提供了一种方便的方法来实现迭代器协议，而不需要必须实现__iter__()和__next__()两个迭代器协议方法。
# 生成器的定义方式有两种，一种是调用生成器函数(yield)，一种是使用生成器表达式语法。

[x*x for x in range(5)] #[0, 1, 4, 9, 16]    列表生成式
(x*x for x in range(5)) #<generator object <genexpr> at 0x00000000021605F0>    generator
# 可以通过next()函数获得generator的下一个返回值：
g=(x*x for x in range(5))
next(g) #每次生成下一个
next(g)
for i in g:
    print(i)
print("-----------------")

""" yield部分 """
# 生成器函数，功能返回数字0-9的平方数
def squares():
    for i in range(10):
        yield i**2  # 使用return关键字是普通函数，使用yield关键字函数变成了生成器函数

g=squares()
from collections.abc import Iterator
isinstance(g,Iterator) # True generator类型是迭代器类型
# 说明生成器函数的执行结果确实是生成器，一种特殊的迭代器。
for i in g:
    print (i)

# 和普通迭代器相比，生成器不单简化了迭代器的定义，还在使用效率上有提升。
# 因为生成器在循环时，生成器函数每次只会返回一个结果，然后保持内部状态，所以生成器占用的内存是很小的。

# 全部数据先加载在1个列表上面，内存占用高
# >>> s1 = sum([i for i in range(100000000)])
# Traceback (most recent call last):
#   File "<pyshell#6>", line 1, in <module>
#     s1 = sum([i for i in range(100000000)])
#   File "<pyshell#6>", line 1, in <listcomp>
#     s1 = sum([i for i in range(100000000)])
# MemoryError

# 数据几乎不占内存
# >>> s2 = sum((i for i in range(100000000)))
# >>> s2
# 4999999950000000

# 斐波拉契数列
def fib1(max):  #函数
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b
        n = n + 1
    return 'done'

# fib1(6)
# print(fib1(6))

# 要把fib1函数变成generator，只需要把print(b)改为yield b就可以了，这就是定义generator的另一种方法
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'

print(fib(6)) #<generator object fib at 0x0000000001E005F0>
for i in fib(6):
    print(i)

# 但是用for循环调用generator时，发现拿不到generator的return语句的返回值。
# 如果想要拿到返回值，必须捕获StopIteration错误，返回值包含在StopIteration的value中
g=fib(6)
while True:
    try:
        x=next(g)
        print('g:',x)
    except StopIteration as e:
        print('generator return value:',e.value)
        break

# 函数是顺序执行，遇到return语句或者最后一行函数语句就返回。
# 而generator的函数，# 在每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行。
def odd():
    print('step 1')
    yield 1
    print('step 2')
    yield (3)
    print('step 3')
    yield (5)

def test():
    o=odd()
    next(o)  #step 1
    next(o)  #step 2
    print(next(o))  #step 3
                    #5
    #next(o)  #error,StopIteration
# test()

#生成器
def flatten(nested):
    for sublist in nested:
        for element in sublist:
            yield element

nested=[[1,2],[3,4],[5]]
print(flatten(nested))
for num in flatten(nested):
    print(num)
print(list(flatten(nested)))

#推导式
g=((i+2)**2 for i in range(2,6))
print(g.__next__())  #4**2
print(next(g))       #5**2 同上
print(list(g)) # [6**2,7**2]

#递归生成器
# 生成器是包含yield关键字，当它被调用时，在函数中的代码不会被执行，而会返回一个迭代器，每次请求一个值，就会执行生成器中的代码，
# 直到遇到一个yield或者return语句，yield语句意味着应该生成一个值，return语句意味着
# 生成器要停止执行（不再生成任何东西，return语句只有在一个生成器中使用时才能进行无参数调用）
def flatten1(nested):
    try:
        #不要迭代类似字符串的对象：
        try:nested+'' #将传入的对象与一个字符串拼接
        except TypeError:pass
        else:raise TypeError
        for sublist in nested:
            for element in flatten1(sublist):
                yield element
    except TypeError:
        yield nested

print(list(flatten1([[[1,2,3],[4,]],[5,[6,[7,8]],9]])))
print(list(flatten1([[['foo','bar'],['zhang',]],['ff',['hy',['hell',8]],9]])))

#flatten1用普通函数重写
def flatten1_normal(nested):
    result=[]
    try:
        try:nested+''
        except TypeError:pass
        else:raise TypeError
        for sublist in nested:
            for element in flatten1_normal(sublist):
                result.append(element)
    except TypeError:
        result.append(nested)
    return result

print(flatten1_normal([[[1,2,3],[4,]],[5,[6,[7,8]],9]]))

def A():
    pass
print(A)
print(A())
def simple_generator():
    yield 1
print(simple_generator) #<function simple_generator at 0x0000000002663340>
print(simple_generator()) #<generator object simple_generator at 0x0000000002130580>
print(next(simple_generator()))
print(simple_generator().__next__())
#生成器的函数返回的迭代器可以像其他的迭代器那样使用

def repeater(value):
    while True:
        new=yield value # 这里并不是变量的定义，当运行到yield时就会停止，所以当运行到等号右边的时候就会停止运行，当在次使用next的时候，将会把一个None赋值给new，因为value的值已经在上轮循环中输出。
                        # 这里可以使用num().send()方法将一个新的值赋值给new
        # print(new)
        if new is not None:
            value=new

r=repeater(42)
print(r.__next__())
print(r.send("hello,world!"))
print(r.__next__())


