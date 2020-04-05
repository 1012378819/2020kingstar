# -*- coding:utf-8 -*-  
'''
Created on 2019年12月11日

@author: pei.lu
'''
# 语感
def begin_1():
    # 元组(1,2,3)和集合{4,5,6}合并成一个列表
    a=list((1,2,3))+list({4,5,6})
    print('合并后的list为%s' %a) 
    a.insert(0,7)
    a.append(0)
    print(a)
    a1=[0,1,2,3,4,5,6]
    a2=a1.copy()
    b1=a1.reverse()  # 直接修改了a1的值
    print('反转后的返回值:{}\n反转后的a1:{}\na2的5的索引位置:{}'.format(b1,a1,a2.index(5)))
    a3=[True,False,0,1,2]
    print(a3.count(True),a3.count(False),a3.count(0),a3.count(1),a3.count(2)) #计数中True=1,False=0
    
# begin_1()
       
def  list_1():
    # 从列表['x',True,1,3,'x',None,'x',False,2,True]中删除元素'X'
    a=['x',True,1,3,'x',None,'x',False,2,'True']
    a.pop(2) # 删除索引号为2的元素
    print(a)
    for i in range(a.count('x')): 
        a.remove('x')
    print(a)
    a.clear() # 清空列表元素
    print(a)
    # 删除列表中索引号为奇数（或偶数）的元素
    a1=list(range(10))
    print(a1)
    del a1[::2] # 删除0，2，4，6。。。偶数，剩下奇数
    print(a1)  #[1, 3, 5, 7, 9]
    a2=list(range(10))
    del a2[1::2]
    print(a2)
    a3=list(range(10))
    a3_偶数=a3[::2] # [0, 2, 4, 6, 8]
    a3_奇数=a3[1::2] # [1, 3, 5, 7, 9]
    print(a3_偶数,a3_奇数)
    
# list_1()

def list_2():
    # 对列表做升序降序排列
    a=[20,3,1,55,10,4] # 同 list((20,3,1,55,10,4))
    a.sort(key=None, reverse=False)
    print(a)
    a.sort(reverse=True)
    print(a)
    # 将列表中大于5的元素置为1，其余为0
    a1=[20,3,1,55,10,4]
    res=[1 if item>5 else 0 for item in a1] # 同 list(1 if item>5 else 0 for item in a1)
    print(res)
    # 对二维列表按前一个数、后一个数排序
    a2=[[33,2],[44,11],[5,21],[6,6]]
    print(sorted(a2,key=lambda x:x[0]))
    print(sorted(a2,key=lambda x:x[1]))
    
# list_2()
def list_3():
    # 遍历列表['x','y','z'],打印每个元素以及对应的索引号
    for index,value in enumerate(['x','y','z']):
        print(index,',',value)
    # 把[1,4,6],['x','y','z']转成[(1,'x'),(4,'y'),(6,'z')]
    res=list((a,b) for a,b in zip([1,4,6],['x','y','z']))
    res1=[(a,b) for a,b in zip([1,4,6],['x','y','z'])]
    print(res,res1)
    # 列表插入元素
    a=list(range(10))
    print(a)
    a[3:3]=['x','y','z'] # 在索引为3位置插入
    print(a)
    b=list(range(10))
    b[3:5]=[True,None,'z'] # 替换索引为[3,5)位置元素
    print(b)
    
# list_3()

def list_4():
    l=['fsf','342ggg','what is wrong',(1,2,3,5),'']
    print(max(list(len(i) for i in l)))
    print(min(list(len(i) for i in l)))
    a=['12','4','12356'] 
    len_max=max([len(i) for i in a])
    for item in a:
        print(item.zfill(len_max))  # 左侧补0成同样的长度
    l1=[{5},1,4,'x','None',' ','',0,tuple(),list()]
    print(list(bool(item) for item in l1))
    
# list_4()

def test_list():
    l=[4,5,6,7,9,4]
    print(l.__str__(),type(l.__str__()))
    l2=['aa','bb']
    print(l+l2)
    print(l*3)
    l.append('new')
    l.insert(1,'na')
    l.extend(l2)
    print(l) #append、insert、extend会直接改变原l
    print(l.index(4))  #默认会找第一个出现位置
    print(l.index(5,2)) #从第2个位置开始找4的索引号
    print(l.count(4))
    l.remove('aa') #删除第一个匹配的元素
    print(l)
    del (l[1]) #删除list某元素
    print(l)
    out1=l.pop(3) #移除list中该位置的元素。不传参默认最后一个元素，并返回该值
    print(l,'return value:',out1)
    out2=l.pop() #移除list中该位置的元素。不传参默认最后一个元素，并返回该值
    print(l,'return value:',out2)
    print([m + n for m in 'ABC' for n in 'XYZ'])
    L = ['Hello', 'World', 'IBM', 'Apple']
    print([s.lower() for s in L]) #变小写

# test_list()

def update_list_dict():
    # list copy
    a=[1,2,3]
    b=a
    c=a.copy()
    print(id(b)==id(a)) # 相等，内存中是一个对象
    print(id(c)==id(a)) # 不相等，不同的对象
    a[0]=0
    print(a,b,c)
    # dict copy
    d={'name':'lp','education':'bachelor'}
    d1=d
    d2=d.copy()
    print(d.update({'Telephone':'13012345678'}))
    print(id(d1)==id(d))
    print(id(d2)==id(d))
    print(d,d1,d2,sep='\n')
    
# update_list_dict()

def dict_1():
    # 列表形式返回dict中所有的key，value
    d={'name':'xiaoming','age':18,'salary':15,'hobby':'piano'}
    print([k for k in d.keys()])
    print([v for v in d.values()])
    print([i for i in d.items()])
    for a in d:
        print(a,d[a])
    # 字典追加元素，更新元素值
    d['height']=180
    d.update({'gender':'male'}) # 不存在的key插入
    d.update({'age':20}) # 存在的key覆盖
    print(d)
    print('gender' in d)
    print('education' in d)
    del(d['name'])  # 删除元素
    res=d.pop('salary') # 删除元素,pop与del区别，pop有返回值，返回key对应的value
    print(res) 
    key,value=d.popitem()  # popitem弹出字典随机的项目
    print(key,value)
    print('删除元素后的d:',d)
    d.clear() # 清空字典
    print(d)
    
# dict_1()
def dict_2():
    print(dict.fromkeys(['a','b','c','d'], 0)) #生成字典,默认值为0
    print({}.fromkeys(['name','age'])) #用fromkeys方法给定的key建立新字典，value对应的值为None   
    print(dict([['a',1],['b',2]])) # [['a',1],['b',2]]转成字典
    print(dict((('a',1),('b',2)))) # (('a',1),('b',2))转成字典
    x,y,z=1,2,3
    a,b,c=(1,2,3)
    print(x,y,z,a,b,c)
    items=[('name','jc'),('age',20),('phone','3926')]
    d1=dict(items)
    d2=dict(name='jc',age=21,phone='3976')
    print(d1,d2,sep='\n')
    print("d1's name is %(name)s,age is %(age)d "% d1)
    print(d1.get('name')) # get方法，访问字典中不存在的key，不会报错，会返回None，也可自定义
    print(d1.get('hobby')) # key不存在，d1['hobby']会报错，用get不会
    d2=dict(name='lup',height=1.60)
    d1.update(d2) #update方法可以用一个字典更新另外一个字典，对应存在的key进行替换，不存在的添加到旧字典中
    print(d1)
    
# dict_2()    

#字典迭代
def iter_dict():
    d={'a':1,'b':2,'c':3}
    for k in d:
        print(k,end=',')
    print("")
    print(d.keys(),d.values(),d.items())
    for k in d.keys():
        print(k)
    for v in d.values():
        print(v)
    for v in d.items():
        print(v)
    for k,v in d.items():
        print(k,v)
    for i,value in enumerate(['a','b',3]):# 内置的enumerate函数可以把一个list变成索引-元素对，这样可以在for循环中同时迭代索引和元素本身
        print(i,value)
    for x,y in [(3,'lp'),(5,'cc'),('aa','bb')]:
        print(x,y)

# iter_dict()

def tuple_str_1():
    t=(1,4,8,11,234,44,4)
    print(t.count(4))
    print(t.index(11))
    print(44 in t)
    print(34 in t)
#     t[2]=888 # 报错，字符串是不可变的,区别于list
    print(t[:2]+(888,)+t[2:]) # 元组插入元素方法
    print((*t[:2],888,*t[2:])) # 结果同上
    print("="*20)
    s='abcdfghijk name andriod'
    print(s.index('e'))
    print('d' in s)
    print('x' in s)
#     s[2]='z'  # 报错，字符串是不可变的,区别于list
    print(s[:4]+'e'+s[4:])     # 字符串插入元素方法
    print(s)
    
# tuple_str_1()

def set_1():
    s=set() # 创建集合
    print(s)
    s.update('a','b','c')
    print(s)
    s.remove('a')
    s.add('x')
    s.add('x')  # 重复插入不影响结果，集合元素不重复
    print(s)
    s.clear() # 清空s
    print(s)
    
# set_1()

def set_2():
    # 集合交并补
    s1={'a','b','c','d'}
    s2={'a','x','y'}
    s3={'a','b'}
    print(s1.difference(s2))  # 差集
    print(s1-s2) # 同上
    print(s1.union(s2)) # 并集
    print(s1.intersection(s2)) # 交集
    print(s1.symmetric_difference(s2)) # 并集
    print(s1.isdisjoint(s2)) # 判断是否不包含重复元素，包含就为False
    print(not s1.isdisjoint(s2))
    print(s3.issubset(s1)) # 判断子集
    print(list(set([11,5,33,11,'abc',(3,4,5),'abc',(3,4,5)]))) # 去除列表重复数据
    
# set_2()

def str_1():
    s='AbDEEfddf naMe'
    d='Ancdfmfdsf123'
    print(s.upper())
    print(s.lower())
    print(s.isupper())
    print(s.islower())   
    print(s.swapcase())  # 大小写互换
    print(d.istitle())   # 是否首字母大写外其他全小写 True
    print(d.isdigit())   # 是否全是数字False
    print(d.isalnum())   # 是否全是字母数字True
    print(d.isascii())   # True
    print('='*20)
    s1='this is python'
    print(s1.title())  # 返回每个单词首字母大写
    print(s1.capitalize())  # 返回第一个单词首字母大写
    print(s1.startswith('this'))  
    print(s1.endswith('Python'))  
    print(s1.count('is'))  
    print(s1.find('is'))  # 返回第一次出现的位置索引，未找到返回-1
    print(s1.rfind('is'))  # 返回最后一次出现的位置索引，未找到返回-1
    print(s1.replace('is','are'))  # 
    
# str_1()
def str_2():
    s='this is python'
    s2=r'C:\Users\pei.lu.KINGSTAR\eclipse-workspace\selenium_auto'
    s3='C:\\Users\\pei.lu.KINGSTAR\\eclipse-workspace\\selenium_auto' # 同s2
    print(s.split())
#     print(s2.split('\')) #  \ 是转移字符，语法报错
    print(s2.split('\\'))
    print(s3.split('\\'))
    s1='https://www.cnblogs.com/snailrunning/p/10163159.html'
    print(s1.split('/', 2)[0][:-1])# 提取协议名 https 
    s='abc'
    print('-'.join(s))
    l=['a','b','c']
    print('-'.join(l))
    
# str_2()   
    
def str_3():    
    s3='12,3.5,8.8,666'
    print(list(float(i) if '.' in i else int(i) for i in s3.split(','))) # [12, 3.5, 8.8, 666]
    print(list(s3))  # ['1', '2', ',', '3', '.', '5', ',', '8', '.', '8', ',', '6', '6', '6']
    s4='\t  pythonpython \n'
    print(s4.lstrip())
    print(s4.rstrip())
    print(s4.strip())  # 去除字符串前后空格，默认为空格
    s1='aaadabcdefaa'
    print(s1.strip('aa')) # 去除字符串前后所有a字符 ，结果 dabcdef
# str_3()

def isinstance_1():
    x=list()
    y=tuple()
    z={}
    s=set()
    print(isinstance(x,(list,tuple)))
    print(isinstance(y,(dict)))
    print(isinstance(z,(list,dict)))
    print(isinstance(s,(set,dict)))

# isinstance_1()

def t():
    keys=['x','y','z']
    values=['1','2','3']
    print(dict(zip(keys,values))) # 等长键列表和值列表转为字典
    print([(a,b) for a,b in zip(['x','y','z'],[1,4,6])])
    print([[a,b] for a,b in zip(['x','y','z'],[1,4,6])])
    print([{a:b} for a,b in zip(['x','y','z'],[1,4,6])])
    print([{a,b} for a,b in zip(['x','y','z'],[1,4,6])])
    a=[8,5,22,14,5,5,4,16]
    v_max=max(set(a),key=a.count)
    print(v_max,a.count(v_max))  # 出现频率最高的数字及次数
    # 二维列表转为一维列表
    print(sum([[1],['a','b'],[1,2,3,4,5]],[])) # [1, 'a', 'b', 1, 2, 3, 4, 5]
    
# t()
def t1():
    l=[1,4,3,22,11]
    print(max(l),min(l),sum(l))
    a=()
    print(dir(a))
    print(eval('3*15+6'))
#     d='x={"name":"Tom","age":16}'
#     exec('x={"name":"Tom","age":16}')  # 在idle执行不报错
#     print(x)
    print([item for item in map(lambda x:pow(x,1/3),[9,3,64,8,27])]) # map()返回迭代器
    print(item for item in map(lambda x:pow(x,1/3),[9,3,64,8,27])) # <generator object t1.<locals>.<genexpr> at 0x0000000002E93EC8>
    
# t1()

def set1():
    # set 唯一、无序
    num={('a','b','c'),1,5,3,'abc','dd',5,1,'dd'}
    print(num)
    num2=set([1,4,5,6,6,5])
    print(num2)
    num1=[11,41,5,6,6,5]
    print('list 去重：',num1,'---->',list(set(num1)))
    temp=set(num1)
    temp.add(666)
    temp.remove(11)
    print(temp)
    # 不可变集合
    num3=frozenset([1,2,3,4,5])
    num3.add(6) # 报错，不可变
    
# set1()











