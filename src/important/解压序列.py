list_a = ['begin', 3, 5, 6, 22, 8, 12, 'end']

# 需求：只要开头和结尾的数值
# *代表中间所有的  _代表一个变量，因为我们不想要了，所以使用_，*后面必须跟一个变量
a, *_, c = list_a
print(a,c)

a, *d, c = list_a
print(d)
# [3, 5, 6, 22, 8, 12]

a,b,*rest=[1,2,3,4]
print (a,b,rest)
a,b,*rest=1,2,3,4
print (a,b,rest)

# 针对dict序列解包获得key和value
#法1
dict1 = {"one":1,"two":2,"three":3}
x,y,z = dict1
print("key-x:",x)
print("key-y:",y)
print("key-z:",z)
print(dict1[x],dict1[y],dict1[z])
#法2
dict1 = {"one":1,"two":2,"three":3}
x,y = dict1.popitem() # popitem弹出字典随机的项目
print("key:",x,"value:",y)

f1 = 1
f2 = 2
# 需求把f1和f2的值进行交换
f1, f2 = f2, f1
print(f1, f2)

# 针对字符串:
a,b,c='hel'
print(a,b,c)
*a,b,c='bcddd'
print(a,b,c)

x,y,z = 1,2,3
print(x,y,z,sep=";;",end="\n\n")
name = ("qiaobushi","wanglihong","leibushi")
x,y,z = name
print(x,y,z)

a=["a",'b','c']
b=("a",'b','c')
c={'a':1,'y':'abc'}
d=[[1,2],[3,4],[5,6]]
print(*a)
print(*b)
print(*c)
print(*d) # [1, 2] [3, 4] [5, 6]

def add(x,y):print(x+y)
l=(1,2)
print(*l)
add(*l)

def story(**kws):
    print('once upon a time ,there was a %(job)s called %(name)s.' %kws)

story(name='Gumby',job='king')
params={'job':'language','name':'python'}
story(**params)
del params['job']
print(params)
story(job='stroke of genius',**params)