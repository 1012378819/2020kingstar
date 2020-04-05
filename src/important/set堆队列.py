from heapq import *
from time import strftime, localtime


def set():
    print(set(range(10)))
    print(set([0,2,3,4,1,3,4]))
    print(set(['fee','fie','foe']))
    a=set([1,2,3])
    b=set([2,3,4])
    print(a.union(b))
    print(a|b)
    print(a & b)
    c=a&b
    print(c.issubset(a))
    print(a.difference(b))

def heap():
    from random import shuffle
    data=range(10)
    # print(shuffle(data))
    # heap=[]
    # for n in data:
    #     heappush(heap,n)
    # print(heap)
    # heappush(heap,0.5)
    # print(heap)

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





