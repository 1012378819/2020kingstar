# import exceptions
# dir(exceptions)
# 系统自带的内建异常类：
# ['ArithmeticError', 'AssertionError', 'AttributeError', 'BaseException', 'BufferError', 'BytesWarning', 'DeprecationWarning',
# 'EOFError', 'EnvironmentError', 'Exception', 'FloatingPointError', 'FutureWarning', 'GeneratorExit', 'IOError', 'ImportError',
# 'ImportWarning', 'IndentationError', 'IndexError', 'KeyError', 'KeyboardInterrupt', 'LookupError', 'MemoryError', 'NameError',
# 'NotImplementedError', 'OSError', 'OverflowError', 'PendingDeprecationWarning', 'ReferenceError', 'RuntimeError', 'RuntimeWarning',
#  'StandardError', 'StopIteration', 'SyntaxError', 'SyntaxWarning', 'SystemError', 'SystemExit', 'TabError', 'TypeError', 'UnboundLocalError',
# 'UnicodeDecodeError', 'UnicodeEncodeError', 'UnicodeError', 'UnicodeTranslateError', 'UnicodeWarning', 'UserWarning', 'ValueError', 'Warning',
# 'WindowsError', 'ZeroDivisionError', '__doc__', '__name__', '__package__']
def divtest():
    while True:
        a = input('输入被除数')
        b=input(u'输入除数')
        try:
            print(int(a)/int(b))
        except Exception as e:
            print('除数不能为0或者类型错误或者其他。。。')
            print(e)
        else:  #没有异常引发的情况执行break退出
            break
        finally: #不论有没有异常都执行
            print("i am always be run")

# divtest()

a1=1
a2=[]
b=2
def A(a,b):
    try:
        a.append(b)
    except AttributeError as e:
        print('a不是一个列表')
    else:
        print(a)
    finally:
        print('finish')

A(a1,b)
A(a2,b)

class A:
    isClose=False #设置默认关闭屏蔽异常
    def cal(self,expr):
        try:
            return eval(expr)
        except ZeroDivisionError:
            if self.isClose:
                print('除数不能为0')
            else:
                raise
c=A()
print(c.isClose)
c.cal('123/11')
c.cal('11/0')
c.isClose=True  #开启屏蔽 or A.isClose=True 同样可以
print(c.isClose)
c.cal('11/0')

#测试文件打开关闭
def testopen():
    try:
        f=open("x.py")
    except:
        print("fail to open")
        exit(-1)
    finally: #防止程序抛出异常最后不能关闭文件，但是需要关闭文件有一个前提就是文件已经打开了。
        f.close()

class OldBoyError(Exception):  # 自定义错误类型
    def __init__(self,message):
        self.message=message
    def __str__(self):  # 打印异常的时候会调用对象里面的__str__方法返回一个字符串
        return self.message
try:
    raise OldBoyError("我错了...")  # raise是主动抛出异常，可以调用自定义的异常抛出异常
except OldBoyError as e:
    print(e)
# 执行结果：我错了...