# 类似__xxx__这样的变量是特殊变量，可以被直接引用，但是有特殊用途，比如上面的__author__，__name__就是特殊变量，
# hello模块定义的文档注释也可以用特殊变量__doc__访问，
# 我们自己的变量一般不要用这种变量名；类似_xxx和__xxx这样的函数或变量就是非公开的（private），不应该被直接引用，比如_abc，__abc等；
# 之所以我们说，private函数和变量“不应该”被直接引用，而不是“不能”被直接引用，是因为Python并没有一种方法可以完全限制访问private函数或变量
# 但从编程习惯上不应该引用private函数或变量。private函数或变量不应该被别人引用

def _private_1(name):
    return 'Hello, %s' % name

def _private_2(name):
    return 'Hi, %s' % name

def greeting(name):
    if len(name) > 3:
        return _private_1(name)
    else:
        return _private_2(name)
# 我们在模块里公开greeting()函数，而把内部逻辑用private函数隐藏起来了，这样，调用greeting()函数不用关心内部的private函数细节，
# 这也是一种非常有用的代码封装和抽象的方法，即： 外部不需要引用的函数全部定义成private，只有外部需要引用的函数才定义为public