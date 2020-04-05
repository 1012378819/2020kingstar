# -*- coding: utf-8 -*-
"""
@time: 2020/2/21 16:58
@author: pei.lu
"""
# https://www.cnblogs.com/sesshoumaru/p/python-iterator.html
# 指能够被内置函数next调用并不断返回下一个值，直到最后抛出StopIteration错误表示无法继续返回下一个值的对象称为迭代器(Iterator)

# 以上的说法只是侠义上的迭代器的定义，在python中，迭代器还需要实现可迭代接口(Iterable)，可迭代接口需要返回的是一个迭代器对象，
# 这样迭代器就能够被for语句进行迭代。
# 在python中，没有内置迭代器类型的对象，但是可以通过内置函数iter将str、tuple、list、dict、set等类型转换成一个迭代器对象。

# >>> s = 'abc'
# >>> next(s)
# Traceback (most recent call last):
# File "<pyshell#27>", line 1, in <module>
#     next(s)
# TypeError: 'str' object is not an iterator
# 以上报错信息可以看出`str`不是迭代器
# >>> it_s = iter(s)
# >>> next(it_s)
# 'a'
# >>> next(it_s)
# 'b'
# >>> next(it_s)
# 'c'
# >>> next(it_s)
# Traceback (most recent call last):
# File "<pyshell#31>", line 1, in <module>
#     next(it_s)
# StopIteration
# 以上报错信息可以看出`iter(str)`是迭代器
# 通过不断的调用next(iterator)方法来获取下一个值，不方便，更为简洁的方法，即for循环。
# for循环每执行一次即相当于调用了一次next(iterator)方法，直到捕获到StopIteration异常退出循环。
#
# >>> it_s = iter(s)
# >>> for c in it_s:
#     print(c)
#
# a
# b
# c

# 以上的例子是使用for循环遍历迭代器
# 模块collections中的类型Iterator就是迭代器的抽象基类，所有的迭代器都是Iterator的实例。
# 即如果一个对象是Iterator的实例，则说明此对象是迭代器。

# from collections.abc import Iterator
#
# >>> isinstance(s,Iterator)
# False
# >>> isinstance(it_s,Iterator)
# True
# 以上信息证实了`str`不是迭代器，而`iter(str)`是迭代器

# 如何自己实现一个迭代器
# 根据python鸭子类型的特性，我们自定义的类型中，只要实现了__next()__方法，该方法在每次被调用时不断返回下一个值，
# 直到无法继续返回下一个值时抛出StopIteration异常即可(next(iterator)实际上调用的是iterator内部的__next()__方法)。
# 迭代器类型Iterator继承自可迭代类型Iterable，可迭代Iterable继承自object基类，迭代器Iterator类型包含__iter()__和__next()__方法，
# 而可迭代类型Iteratble仅仅包含__iter__()。可迭代对象，通过__iter()__返回一个迭代器对象，迭代器对象的__next()__方法则实际用于被循环。
class MyIter():
    def __init__(self,max_value):
        self.current_value = 0
        self.max_value = max_value

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_value < self.max_value:
            result = self.current_value
            self.current_value += 1
            return result
        else:
            raise StopIteration

# 验证对象是否可以用于for循环
#
# >>> my_iter = MyIter(3)
# >>> for i in my_iter:
# print(i)

# 验证对象是否是Iterator实例
#
# >>> from collections.abc import Iterator
# >>> isinstance(my_iter,Iterator)
# True


# 总结
# 凡是可作用于for语句循环的对象都是Iterable可迭代类型。
# 凡是可作用于next()函数的对象都是Iterator迭代器类型。
# str、tuple、list、dict、set等类型是Iterable可迭代类型，但不是Iterator迭代器；可以通过iter()函数获得一个Iterator对象。
# 通过Iterable可迭代类型的__iter()__方法可以获得一个Iterator迭代器对象，从而使得它们可以被for语句循环。
# Python的for循环本质上就是通过调用Iterable可迭代对象的__iter()__方法获得一个Iterator迭代器对象,然后不断调用Iterator迭代器对象__next()__方法实现的
