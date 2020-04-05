# -*- coding:utf-8 -*-
"""
Created on 2019年12月21日

@author: pei.lu
"""

# 闭包
import math


def power(x):
    def closures(y):
        return pow(y,x)
    return closures

power2=power(2) # 计算平方的函数
power3=power(3) # 计算立方的函数
# print(power2(power3(2))) # (2**3)**2

# 距离具体时刻的时分秒
def exercise_1():
    from datetime import datetime
    now=datetime.now()
    new_year=datetime(2021,1,1,0,0,0) # 2021年元旦
    delta=new_year-now
    all_secds=delta.total_seconds() # 获取时间间隔的总秒数
    days=delta.days
    times=divmod((all_secds-days*60*60*24),60*60) # 获取除去天数的小时数
    mins_and_sec=divmod(times[1],60) # 获取除去天数的小时数
    print(days,times[0],mins_and_sec[0],mins_and_sec[1])

# exercise_1()

# 计算频率最高的3个字符
def exercise_2():
    content="""The Image module provides a class with the same name which is
    used to represent a PIL image. The module also provides a number
    of factory functions, including functions to load images from files,
    and to create new images."""
    set_element=set(list(content))
    stat=[(e,content.count(e))  for e in set_element]
    print(stat)
    top_3_element=sorted(stat,key=lambda x:x[1],reverse=True)[:3]
    print('top3频率的词和频率为：',top_3_element)

# exercise_2()

# 猜数字
def num_game():
    from random import randint
    num=randint(1,1000)
    first,last=1,1000
    while True:
        guess_num=int(input("猜一个数字"))
        if num!=guess_num:
            if num<guess_num:
                last=guess_num
            else:
                first=guess_num
            print('num are in [%d,%d]'%(first,last))
        else:
            print('bingo,you are right')
            break

# num_game()
def num_game_2():
    input('请在心中默记一个小于1000的正整数\n我来猜猜看\n敲回车键开始')
    n_min, n_max = 1, 999
    mid = n_min + (n_max - n_min) // 2
    while True:
        reply = input('我猜是%d，对吗？' % mid)
        if reply == '=':
            print('哈哈，我猜对了！')
            break
        elif reply == '+':
            n_min, n_max = n_min, mid - 1
            mid = n_min + (n_max - n_min) // 2
        elif reply == '-':
            n_min, n_max = mid + 1, n_max
            mid = n_min + (n_max - n_min) // 2
        else:
            print('你只能回答加号、减号或等号！')

# num_game_2()

# 判断正整数包含数字7
def judge_contain_7():
    a=98790
    list_num=str(a)
    print('7' in list_num)

# judge_contain_7()

## 生成26的小写字母
# [chr(ord('a')+i) for i in range(26)]

# 偏移固定值制造加解密算法
def encrypt_decrypt(text,key):
    """加密/解密算法"""
    # ord()函数可以把字符转成对应ASCII码，chr()是逆运算,ord('A')=65,chr(65)='A'
    result=list()
    for ch in text:
        if 'a'<=ch <='z': # 偏移小写字母
            num_ascii=(ord(ch)-ord('a')+key)%26+ord('a') # 偏移后新字母的ASCII码值
            ch_new=chr(num_ascii) # 加密后的新字母
            result.append(ch_new)
        elif 'A'<=ch <='Z':
            num_ascii = (ord(ch) - ord('A') + key) % 26 + ord('A')  # 偏移后新字母的ASCII码值
            ch_new = chr(num_ascii)  # 加密后的新字母
            result.append(ch_new)
        else:
            result.append(ch) # 字母外的其他字符不变

    return ''.join(result)

# print(encrypt_decrypt('aBc123xYz',5))
# print(encrypt_decrypt('fGh123cDe',-5))

def exampe():
    from itertools import permutations,combinations # 排列组合函数
    option=[1,2,3,4,5]
    for i in permutations(option,len(option)):
        print(i)
    for opt in permutations(option,4):  # 排列函数
        print(opt)
    print(len(list(permutations(option,4))))  #5*4*3*2=120
    for opt in combinations(option,4):  # 组合函数
        print(opt)
    print(len(list(combinations(option,4))))  #5*4*3*2/(4*3*2*1)

exampe()
# 交换字符串中值
def execrise_swap_character():
    phase=10*'w'+10*'-'+10*'b'
    print(phase)
    a,b=phase.index('-'),phase.index('b')
    phase=list(phase)
    phase[a],phase[a-1]=phase[a-1],phase[a]  # list支持交换值方法，str不自持这种交换方法
    # phase[b],phase[b-1]=phase[b-1],phase[b]
    print(phase[b-1:b+1],phase[b:b-2:-1])   # 注意的逆序取部分值的表示
    phase[b-1:b+1]=phase[b:b-2:-1]
    print(''.join(phase))
# execrise_swap_character()

# 按总分高低排序，总分一致按英语、数学、物理高低排序
def sorted_example():
    grade = [
        {'name':'Lucy', 'math':85, 'english':82, 'physics':93},
        {'name':'Alice', 'math':90, 'english':85, 'physics':97},
        {'name':'David', 'math':77, 'english':95, 'physics':86},
        {'name':'Irene', 'math':95, 'english':85, 'physics':92}
    ]
    for item in grade:
        item.update({'total':item['math']+item['english']+item['physics']})
    print(grade)
    for item in sorted(grade,key=lambda x:(x['total'],x['math'],x['physics']),reverse=True):
        print(item)

# 打印蛇形矩阵
def print_she_matrix(width):
    for i in range(1,width+1):
        for j in range(i+1,width+2):
            print(1+sum(range(1,i))+sum(range(i+1,j)),end=' ')
        print()

# print_she_matrix(5)

# ABCDE*G=EDCBA
def test_1():
    import time
    from itertools import permutations
    b_time=time.time()
    nums_str='0123456789'
    l=list(nums_str)
    for item in permutations(l,5):
        item=list(item)
        num_b=int(''.join(item))
        num_e=int(''.join(item[::-1]))
        x,y  = divmod(num_e, num_b)
        if y==0 and str(x) in nums_str:
            print(num_b,'*',int(num_e)//int(num_b),'=',num_e)
    e_time=time.time()
    print(e_time-b_time)
# test_1()
# ABCDE*G=EDCBA
def test_2():
    import time
    b_time=time.time()
    for i in range(10000,100000):
        a,x=divmod(i,10000)
        b,x=divmod(x,1000)
        c,x=divmod(x,100)
        d,e=divmod(x,10)
        if len(set([a,b,c,d,e]))==5:
            for j in range(1,10):
                k=10000*e+1000*d+100*c+10*b+a
                if(i*j==k):
                    print(i,'*',j,'=',k)
    e_time=time.time()
    print(e_time-b_time)
# test_2()

# 二维数组反转
# [[1,2,3,4],[7,8,9,10]]--->[[1, 7], [2, 8], [3, 9], [4, 10]]
def arr_reverser(arr):
    rows=len(arr)
    if rows==0:
        return list()
    if [isinstance(item,list) for item in arr].count(True)!=rows:
        return list()
    cols=len(arr[0])
    if [len(item) for item in arr].count(cols)!=rows:
        return list()
    res = list()
    for i in range(cols):
        a = list()
        for j in range(rows):
            a.append(arr[j][i])
        res.append(a)
    return(res)
#print(arr_reverser([[1,2,3,4],[7,8,9,10]]))
# print(arr_reverser([[],[1,2,3]]))

# 十进制数转为二进制数
def func(n,first=True):
    if n==0:
        if first:
            return '0b0'
        else:
            return '0b'
    return str(func(n//2,False))+str(n%2)

# 十进制浮点数转为二进制数
def bin_float(n,prec=10):  # 默认值10，限制二进制小数后最多取10位
    num_int=int(n)
    num_dec=n-num_int
    s=''
    while num_dec>0 and len(s)<prec:
        num_dec*=2
        if num_dec>=1:
            s+='1'
            num_dec-=1
        else:
            s+='0'
    print('%s.%s'%(bin(num_int),s))

# bin_float(3.14)
def bin_decimal(bin_str):
    """二进制字符串转十进制浮点数"""

    num_int, num_dec = bin_str.split('.')

    s = int(num_int, base=2)
    for i, bit in enumerate(num_dec):
        if bit == '1':
            s += math.pow(2, -(i + 1))
    return s

# 统计文件夹以.py结尾文件总行数(广度优先原则)
def count_code_data(folder):
    """以广度优先方式遍历，统计.py文件的代码总行数"""
    import os
    total=0
    for root,dirs,files in os.walk(folder,topdown=True): # topdown=True为广度优先。深度优先（topdown=False）
        for f in files:
            name,ext=os.path.splitext(f)
            if ext=='.py':
                fn=os.path.join(root,f)
                with open(fn,'r',encoding='utf-8') as fp:
                    lines=len(fp.readlines())
                    total+=lines
                    print(fn,lines)
    return(total)

# 过滤序列
def test():
    a=[-2.5,5,1,0,-3]
    b=[i for i in a if i>=0]
    c=[i if i>=0 else None for i in a ]
    d=list(filter(lambda x:x>=0,a))
    print(b,c,d,sep='\n')
# test()

# 统计字符数并排序
def count_char(s):
    ch = set(s)
    y = [(i, s.count(i)) for i in ch]
    d = sorted(y, key=lambda x: x[1], reverse=True)
    print(y, d, sep='\n')

def count_char_1(s):
    ch = set(s)
    num = list(map(s.count,ch))
    d = sorted(zip(ch,num), key=lambda x: x[1], reverse=True)
    print(d, sep='\n')

def count_char_2(s):
    from collections import Counter
    print(Counter(s))

# 转换字符大小写，大写字符多转为大写，小写字符多转为小写
s="puFHFFSSFff"
def transfer_s(s):
    upper=sum(i.isupper() for i in s)
    lower=sum(i.islower() for i in s)
    return [s.lower(),s.upper()][upper>=lower]
# print(transfer_s(s))

# 根据日期返回星期几
def func_return_weekday(date_str):
    import time
    week=['一','二','三','四','五','六','日']
    try:
        day=time.strptime(date_str,'%Y-m-%d')
        wday=day.tm_wday
        return '星期'+week[wday]
    except:
        return '格式不正确'

def func_return_weekday_1(date_str):
    from datetime import datetime
    week = ['一', '二', '三', '四', '五', '六', '日' ]
    try:
        day=datetime.strptime(date_str,'%Y-%m-%d')
        wday=day.weekday()
        return '星期'+week[wday]
    except:
        return '格式不正确'

print(func_return_weekday('2020-4-3'))
print(func_return_weekday_1('2020-4-3'))

# 判断是否二的幂方（2、4、8、16。。。）
def judge_ismi(num):
    while num!=1:
        if num%2!=0:
            print('not!')
            break
        else:
            num=num//2
    else:
        print('yes!')

# 判断相邻两数相同，就置后者为两数和，并删除前者
# a=[8,2,4,2,2,4,2]
# i=1
# while i<len(a):
#     if a[i]==a[i-1]:
#         a[i]+=a[i-1]
#         a.pop(i-1)
#         i-=1
#     else:
#         i+=1
# print(a)


# eval()与exec()差异
# 内置函数eval()接受一个字符串格式的Python表达式参数，直接运行表达式，返回表达式的求值结果。可以用eval()函数计算从键盘读入的四则运算表达式。
# 内置函数exec()接受一个字符串格式的Python表达式，直接运行表达式，不返回表达式的求值结果。可以用exec()函数完成从键盘读入的python赋值表达式。当然，exec()也可以执行其他无返回的Python语句。
# >>> expression = input('请输入四则运算表达式：')
# 请输入四则运算表达式：2*(3+5)-4
# >>> expression
# '2*(3+5)-4'
# >>> eval(expression)
# 12
# >>> expression = input('请输入python赋值表达式：')
# 请输入python赋值表达式：x = [1,2,3]
# >>> expression
# 'x = [1,2,3]'
# >>> exec(expression)
# >>> x
# [1, 2, 3]
# >>> exec('x.sort(reverse=True)')
# >>> x
# [3, 2, 1]
