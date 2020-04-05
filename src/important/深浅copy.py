# 总结：
# 浅复制是共享内存，深复制则是独享。
# 不论针对列表还是字典，浅拷贝时，修改的元素类型是可变类型时，他变我也变，修改的类型是不可变类型时，他变我不变。
#
# 不论针对列表还是字典，深拷贝时，他变我不变。
#
# 可变类型：字典、列表。
#
# 不可变类型：整型、字符串、元组。

# 浅拷贝
## list类型
'''
浅拷贝方法：
1、a = b[:]
2、a = b.copy()
3、引用copy模块，import copy  |  a = copy.copy(b)
'''

wife = ['diaoqian', 1988, ['slaras', 10000]]
hasband = wife[:]

print(wife, hasband)  # ['diaoqian', 1988, ['slaras', 10000]]    ['diaoqian', 1988, ['slaras', 10000]]

hasband[0] = 'zhaoyun'
hasband[2][1] = 2000

print(hasband)# ['zhaoyun', 1988, ['slaras', 2000]]
print(wife)# ['diaoqian', 1988, ['slaras', 2000]]

'''
浅拷贝原则：
1、只复制一层，他变我不变，其余层，他变我也变。
2、如果只有一层，就相当于深复制了
'''

# 深拷贝

'''
深拷贝方法：
1、引用copy模块，import copy  |  a = copy.deepcopy(b)
'''

import copy

wife = ['diaoqian', 1988, ['slaras', 10000]]
hasband = copy.deepcopy(wife)

print(wife, hasband) # ['diaoqian', 1988, ['slaras', 10000]]   ['diaoqian', 1988, ['slaras', 10000]]

hasband[0] = 'zhaoyun'
hasband[2][1] = 8000

print(hasband)# ['zhaoyun', 1988, ['slaras', 8000]]
print(wife)# ['diaoqian', 1988, ['slaras', 10000]]

'''
深拷贝小结：
1、深度拷贝就是克隆一份，具有自己单独的内存地址，两者完全不相干设，他变我不变。
'''

## dict类型

# 浅拷贝

wife = {'name': {'diaoq': 30}, 'slaras': 10000}
hasband = copy.copy(wife)

print(hasband, wife) # {'name': {'diaoq': 30}, 'slaras': 10000}   {'name': {'diaoq': 30}, 'slaras': 10000}

hasband['name']['diaoq'] = 32
hasband['slaras'] = 12000

print(hasband)# {'slaras': 12000, 'name': {'diaoq': 32}}
print(wife)# {'slaras': 10000, 'name': {'diaoq': 32}}


# 深拷贝

wife = {'slaras': 10000, 'name': {'diaoq': 30}}
hasband = copy.deepcopy(wife)

print(hasband, wife)
# {'name': {'diaoq': 30}, 'slaras': 10000}  {'name': {'diaoq': 30}, 'slaras': 10000}

hasband['name']['diaoq'] = 32
hasband['slaras'] = 12000

print(hasband)# {'slaras': 12000, 'name': {'diaoq': 32}}
print(wife)# {'slaras': 10000, 'name': {'diaoq': 30}}

#其他例子：
a=[1,2,3,4]
b=a[:] #切片copy，浅拷贝
c=a #当你创建一个对象并给它赋一个变量的时候，这个变量仅仅 参考 那个对象，而不是表示这个对象本身！变量名指向你计算机中存储那个对象的内存。称作名称到对象的绑定。
print('a=',a,'b=',b,'c=',c)
del a[0]
print('a=',a,'b=',b,'c=',c)

#如果你想要复制一个列表或者类似的序列或者其他复杂的对象（不是如整数那样的简单 对象 ），那么你必须使用切片操作符来取得拷贝。
#如果你只是想要使用另一个变量名，两个名称都 参考 同一个对象,用赋值

# 将一个列表的数据复制到另一个列表中。

a=[1,2,3,4,['a','b']]
b=a
c=a[:]
d=copy.copy(a)
e=copy.deepcopy(a)
for i in [b,c,d,e]:
    print(id(a)==id(i)) # 判断内存中是不是同一地址
a.append(5)
a[4].append('c')
print(a,b,c,d,e,sep='\n')

#深浅拷贝
def B():
    from copy import deepcopy
    d={}
    d['name']=['lup','jc','tt']
    d['age']=50
    d_cy=d.copy()
    d_deepcy=deepcopy(d)
    d['age']=18   #替换d的age，不是修改某个值。
    d['name'].append('ss')
    print('       d:',d,'\n','    d_cy:',d_cy,'\n','d_deepcy:',d_deepcy,sep="")

# B()
