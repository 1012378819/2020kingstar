def A(a):
    def B(b):
        print (a*b)
    return B

# double=A(2)
# print(double) # <function A.<locals>.B at 0x0000000003448A68>
# double(3)     # 6
# A(3)(5)       # 15

def cal_sum(*args):
    ax=0
    for n in args:
        ax=ax+n
    return ax

# 如果不需要立刻求和，而是在后面的代码中，根据需要再计算怎么办？可以不返回求和的结果，而是返回求和的函数，如下：
def lazy_sum(*args):
    def sum():
        ax=0
        for n in args:
            ax=ax+n
        return ax
    return sum #返回函数

f=lazy_sum(1,3,5,7,9)
print(f) #<function lazy_sum.<locals>.sum at 0x00000000021E3340>
print(f())
# 我们在函数lazy_sum中又定义了函数sum，并且，内部函数sum可以引用外部函数lazy_sum的参数和局部变量，当lazy_sum返回函数sum时，
# 相关参数和变量都保存在返回的函数中，这种称为“闭包（Closure）”的程序结构拥有极大的威力。
# 注意，当调用lazy_sum()时，每次调用都会返回一个新的函数，即使传入相同的参数：
#
# >>> f1 = lazy_sum(1, 3, 5, 7, 9)
# >>> f2 = lazy_sum(1, 3, 5, 7, 9)
# >>> f1==f2
# False

"""偏函数"""
#默认转换字符串为2进制整数
def int2(x, base=2):
    return int(x, base)

# functools.partial帮助创建一个偏函数，不需要自定义int2（）
import functools

int3=functools.partial(int,base=2)
# 简单总结functools.partial的作用就是，把一个函数的某些参数给固定住（也就是设置默认值），返回一个新的函数，调用这个新函数会更简单


