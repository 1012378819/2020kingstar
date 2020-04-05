# -*- coding: utf-8 -*-
"""
@time: 2020/4/4 11:20
@author: pei.lu
"""
# collections模块
from collections import Counter
print(Counter(['a','b','a','d','aa','b','a'])) # 返回字典，值为迭代对象的元素计数
print(Counter('abcdabcaba')) # 返回字典，值为迭代对象的元素计数
d=Counter('hello world')
print(d.most_common(2)) # [('1',3),('0',2)]

s='abc'
it_s=iter(s)
from collections.abc import Iterator
print(isinstance(s,Iterator)) # False
print(isinstance(it_s,Iterator)) # True

from collections import deque
def dequeue():
    q=deque(range(5))
    print(q)
    q.append(8) #右侧入队列
    q.appendleft(6) #左侧入队列
    print(q)
    print(q.pop())
    print(q.popleft())
    print(q)
    q.rotate(2) #顺时针旋转
    print(q)
    q.rotate(-1)
    print(q)
dequeue()

from  collections import OrderedDict
content=OrderedDict() # 有序字典，可记住键值对的添加顺序
content['name']='zhangsan'
content['age']=20
content['male']='yes'
content['hobby']='piano'
print(content,type(content))

from functools import reduce # py3的reduce需要引入
from itertools import combinations,permutations # 分别为组合、排列