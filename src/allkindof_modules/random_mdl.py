# -*- coding: utf-8 -*-
"""
@time: 2020/2/27 8:51
@author: pei.lu
"""
import random,pprint
def testRandom():
    print(random.random())  # 返回[0,1)内的随机数
    print(random.uniform(-10,10))  #返回[-10,10]内随机实数n
    print(random.randint(1,10))  #返回[1,10]内随机整数
    print(random.randrange(1,10,2)) #返回range(start,stop,step)中的随机数
    print(random.choice('ancdefg'))    # 返回序列的随意元素
    print(random.choice((1,'2n',3,'adf','fs')))
    print(random.sample('ancdefg',2) ) # 从序列中选择n个随机独立的元素
    values=range(1,11) #+ 'jack queen king'.split()
    suites='diamond clubs hearts spades'.split()
    deck=['%s of %s ' % (v,s) for v in values for s in suites]
    print(deck)
    random.shuffle(deck) # 进行序列的乱序
    pprint.pprint(deck[:12])

testRandom()
