# -*- coding: utf-8 -*-
#@time: 2019/12/1 19:40
#@author: pei.lu
# print(filter(None,[1,0,False,True]))
# print(list(filter(None,[1,0,False,True])))
# print(list(filter(None,range(10))))
# print(list(filter(lambda x:x%2,range(10))))
#
# print(list(map(lambda x:x*2,range(10))))
def factorial(n): # 迭代
    res=n
    for i in range(1,n):
        res*=i
    return res

def fac(n): # 递归
    if n==1:
        return 1
    else:
        return n*fac(n-1)

# 斐波那契
def fabonaci(n): #递归
    if n<1:
        return -1
    if n==1 or n==2:
        return 1
    else:
        return fabonaci(n-1)+fabonaci(n-2)

def fab(n): #迭代
    n1=1
    n2=1
    n3=1
    if n<1:
        return -1
    while (n-2)>0:
        n3=n2+n1
        n1=n2
        n2=n3
        n-=1
    return n3

# 汉诺塔
def hanoi(n,x,y,z): # 将n的盘子从x移动到z，借助y
    if n==1:
        print(x,'-->',z)
    else:
        hanoi(n-1,x,z,y) # 将前n-1个盘子从x移动到y上（借助z）
        print(x,'-->',z) # 将最底下的最后一个盘子从x移动到z上
        hanoi(n-1,y,x,z) # 将y上的n-1个盘子移动到z上

#递归 n*(n-1)*(n-2)*...*1
def funcA(n):
    result=n
    for i in range(1,n):
        result=result*i
    print(result)

def funcB(n):
    if n==1:
        return 1
    else:
        return (n*funcB(n-1))
    
# funcA(5)
# print(funcB(5))

#递归实现二元查找
def search(seq,num,lower=0,upper=None): # 在有序seq中查找num所在的索引位置
    if upper is None:
        upper=len(seq)-1
    if lower==upper:
        assert num==seq[upper]
        return upper
    else:
        mid=(lower+upper)//2
        if num>seq[mid]:
            return search(seq,num,mid+1,upper)
        else:
            return search(seq,num,lower,mid)

seq=[2,55,111,3,43,1,-3]
print(seq.sort())  #sort函数没有返回值，返回值为None
print(seq)
print(search(seq,-3))
print(search(seq,43))

# 有一头母牛，每年元旦生一年小母牛，每头小母牛从4周岁开始每年元旦也生一头小母牛，计算n个元旦后，母牛数（不考虑死亡）
def cows_count_1(n):
    """递归"""
    if n<4:
        return n+1
    return cows_count_1(n-4)+cows_count_1(n-1)
print(cows_count_1(20))

def cows_count_2(n):
    """循环"""
    if n<4:
        return n+1
    result=[1,2,3,4]
    for i in range(4,n+1):
        result.append(result[0]+result[-1])
        result.pop(0)
    return result[-1]
print(cows_count_2(20))

# 列表展开
def flatten(lst):
    res=[]
    for i in lst:
        if isinstance(i,list):
            res.extend(flatten(i))
        else:
            res.append(i)
    return res

lst=[[1,5],[412,[676,[7,11,24],[88]]],[3]]
# print(flatten(lst))
