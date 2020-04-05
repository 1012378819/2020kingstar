# -*- coding:utf-8 -*-
'''
Created on 2019年12月12日

@author: pei.lu
'''
# 语感训练合并字典
a={'a':1,'b':2,'c':3}
b={'aa':1,'bb':2,'cc':3}
print('a.items()=',a.items())
for k,v in b.items():
    a[k]=v
print('new dict:',a)

print("============================")

a={'a':1,'b':2,'c':3}
b={'aa':1,'bb':2,'cc':3}
d1_dict=dict(a,**b)
d2_dict=dict(**a,**b)
d3_dict=dict()
d3_dict.update(a)
print('d1_dict={},\nd2_dict={},\nd3_dict={}'.format(d1_dict,d2_dict,d3_dict))

# 合并列表
l1=['a','b','c']
l2=['x','y','z']
print('列表合并:',l1+l2)
l1+=l2
# l1.extend(l2)  # 结果同l1+=l2 ,修改了l1的值
print('修改了l1:',l1)
x=['x1','x2','x3']
y=['y1','y2','y3']
x[0:0] = y # 使用切片实现插入元素
print('插入后的x:',x)
# 合并元组
t1=('a','b','c')
t2=('x','y','z')
print('元组合并：',t1+t2)

