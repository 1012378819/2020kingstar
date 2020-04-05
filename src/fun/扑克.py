# -*- coding:utf-8 -*-
import random,pprint
def puk1():
    a=range(1,14)
    b='hot,het,fk,ch'.split(',') #定义四种类型（红桃、黑桃、方块、草花）
    c=['dw','xw'] #大王、小王
    p=['%s %s '% (x,y)for x in b for y in a] #循环嵌套
    p.extend(c)
    user1=random.sample(p,18) # 从p中输出18张牌
    print(p)
    pprint.pprint(user1)
    random.shuffle(p) # 将序列的所有元素随机排序。
    print(p)
    print(p[:18])

def puk2():
    # 生成扑克牌
    a=['黑桃','红桃','梅花','草花']
    b=list(range(2,11))+['J','Q','K','A']
    c=['大王','小王']
    pk=[i+str(j) for i in a for j in b]+c
    print(pk,len(pk),sep='\n')

# puk2()
# 判断五张扑克是否顺子
def get_five():
    poker=list(range(1,14))*4+[0,0]
    import random
    return random.sample(poker, 5)

#
def is_straight(five):
    no_zero=list(filter(lambda x:x>0,five)) # 剔除0
    if len(no_zero)>len(set(no_zero)):  # 如有重复
        return False   # 不为顺子
    no_zero.sort()  # 排序后直接改变原数组
    import numpy as np
    no_zero=np.array(no_zero) # 转为numpy数组
    diff=np.diff(no_zero)  # 相邻元素差组成的数组
    if np.sum(diff-1)>5-no_zero.size:  # diff各元素-1的和大于0的个数
        return False  # 不是顺子
    else:
        return True








def count():
    fs = []
    for i in range(1, 5):
        def f():
             return i*i
        fs.append(f)
    return fs

f1, f2 ,f3,f4= count()
# print(f1())
# print(f2())

#迭代查找list中的max，min，返回一个tuple
def findMinAndMax(L):
    if len(L)==0:
        return (None,None)
    else:
        min, max = L[0], L[0]
        for i in L:
            if min >i:
                min=i
            if max <i:
                max=i
        return(min,max)

