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