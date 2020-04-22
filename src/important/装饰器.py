# 装饰器本质上是一个Python函数，它可以让其他函数在不需要做任何代码变动的前提下增加额外功能，装饰器的返回值也是一个函数对象。
# 它经常用于有切面需求的场景，比如：插入日志、性能测试、事务处理、缓存、权限校验等场景。
# 有了装饰器，我们就可以抽离出大量与函数功能本身无关的雷同代码并继续重用。
# 装饰器的作用就是为已经存在的函数或对象添加额外的功能。

# 由于函数也是一个对象，而且函数对象可以被赋值给变量，所以，通过变量也能调用该函数。

# 假设我们要增强now()函数的功能，比如，在函数调用前后自动打印日志，但又不希望修改now()函数的定义
# 这种在代码运行期间动态增加功能的方式， 称之为“装饰器”（Decorator）
def now():
    print('2015-3-25')

f = now
f()
print(now.__name__) # now 
print(f.__name__)  # now

# 在早些时候 (Python Version < 2.4，2004年以前)，为一个函数添加额外功能的写法是这样的。
def debug(func):
    def wrapper():
        print("[DEBUG]: enter {}()".format(func.__name__))
        return func()
    return wrapper

def say_hello():
    print("hello!")

say_hello = debug(say_hello)  # 添加功能并保持原函数名不变

# say_hello()

@debug   # 语法糖 等同于  say_hello = debug(say_hello)  # 添加功能并保持原函数名不变
def say_hello_1():
    print("hello!")

# say_hello_1()

# 如果被装饰的函数需要传入参数
def debug_1(func):
    def wrapper(*args, **kwargs):  # 指定宇宙无敌参数
        print("[DEBUG]: enter {}()".format(func.__name__))
        print('Prepare and say...',)
        return func(*args, **kwargs)
    return wrapper  # 返回

@debug_1
def say(something):  #装饰器函数的返回值是wrapper，也就是说现在say是等同于wrapper的。
    print("hello {}!".format(something))

say('stranger,nice to meet me')


# ----------------------------------------------------

# https://blog.csdn.net/qq_41853758/article/details/82853811
# 闭包
def num(num):  # 定义函数
    def num_in(num_in):  # 定义函数
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
