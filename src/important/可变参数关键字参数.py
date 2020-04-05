#由于在args变量前有*前缀，所有多余的函数参数都会作为一个元组存储在args中。如果使用的是**前缀，多余的参数则会被认为是一个字典的键/值对。
def powersum(power,*args):
    ''' return the sum of each argument raised to specified power'''
    total=0
    for i in args:
        total+=pow(i,power)
    print(total)

# powersum(2,3,4) #3^2+4^2
# powersum(3,10,10,10) #10^3+10^3+10^3
# print(powersum.__doc__)
# help(powersum)

# 参数定义的顺序必须是：必选参数、默认参数、可变参数和关键字参数。
# *args是可变参数，args接收的是一个tuple；
# **kw是关键字参数，kw接收的是一个dict。
# 可变参数既可以直接传入：func(1, 2, 3)，又可以先组装list或tuple，再通过*args传入：func(*(1, 2, 3))；
# 关键字参数既可以直接传入：func(a=1, b=2)，又可以先组装dict，再通过**kw传入：func(**{'a': 1, 'b': 2})。
def func(a,b,c=0,*args,**kw):
    print("a=",a,"b=",b,"c=",c,'args=',args,'kw=',kw)

# func(1,2)
# func(1,2,3)
# func(1,2,3,'a','b')
# func(1,2,3,'a','b',x=99)
# a=(1,2,3,4)
# b={'x':99}
# func(*a,**b)


#对于*，**传参例子
def foo(*args):
    print(args)
#
# foo(123)
# foo('a','b','c')
# a=['a','b','c']
# b=('a','b','c')
# c={'a':1,'y':'abc'}
# print(*a,*b,*c)
# foo(a)   #把a作为一个元素传参，整体为tuple的第一个值
# foo(*a)
# foo(b)   #把b作为一个元素传参，整体为tuple的第一个值
# foo(*b)
# foo(c)   #把c作为一个元素传参，整体为tuple的第一个值
# foo(*c)

def fun(**kw):
    print(kw)

# fun(a='aa',b=2)
#
# kv={'a':1,'y':'abc'}
# fun(**kv)



