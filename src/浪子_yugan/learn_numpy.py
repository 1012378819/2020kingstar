# -*- coding: utf-8 -*-
"""
@time: 2020/2/9 11:52
@author: pei.lu
NumPy 是 Python 科学计算的基础软件包，提供了多维数组对象，多种派生对象（掩码数组、矩阵等）以及用于快速操作数组的函数
及 API，它包括数学、逻辑、数组形状变换、排序、选择、I/O 、离散傅立叶变换、基本线性代数、基本统计运算、随机模拟等等
https://mp.weixin.qq.com/s/hLTcnZ_sbEC4Pkvy_jQqtw
"""
# dtype 是数组的属性之一，查看数组的数据类型。创建数组时，如果不指定数据类型，NumPy 会根据输入数据选择合适的数据类型
import numpy as np
a=np.array([0,1,2,3])
b=np.array([0,1,2,3.0])
c=np.array([0,1,2,3+2j])
# print(a.dtype,b.dtype,c.dtype) # int32 float64 complex128

# 分层求和，逐行求和，逐列求和
def knowledge_1():
    a=np.arange(18).reshape((3,2,3)) # 3层2行3列的结构
    print(a)
    # array([[[ 0,  1,  2],
    #         [ 3,  4,  5]],
    #        [[ 6,  7,  8],
    #         [ 9, 10, 11]],
    #        [[12, 13, 14],
    #         [15, 16, 17]]])
    print(np.sum(a)) # 总和
    print(np.sum(a,axis=0)) # 层合并求和
    print(np.sum(a,axis=1)) # 行合并求和
    print(np.sum(a,axis=2)) # 列合并求和
    print(np.sum(np.sum(a,axis=1),axis=1)) # 分层求和方法1
    print(np.sum(np.sum(a,axis=1),axis=0)) # 分层求和方法2
    print(sum(np.sum(np.sum(a,axis=1),axis=0))) # 分层求和后求总和
    print(np.sum(np.sum(np.sum(a,axis=1),axis=0),axis=0)) # 分层求和后求总和2

# 整型数组各元素加1；
# 求两个等长整型数组对应元素之和组成的新数组；
def do_by_python():
    x=list(range(5))
    print(x)
    for item in x:  # 遍历数组为每个元素加1
        x[item]+=1
    print(x)
    y=list(range(5,10))
    z=list()
    for i,j in zip(x,y):    # 遍历两个数组，逐个元素求和
        z.append(i+j)
    print(z)
    print('list直接相加结果（区别于numpy）',x+y)

do_by_python()
def knowledge_2():
    a=np.arange(5)
    print(a)
    a+=1
    print(a)
    b=np.arange(5,10)
    c=a+b
    print(c)

# knowledge_2()

# 用NumPy数组实现起来，要比python数组更简洁、更清晰。这得益于NumPy的两大特性：广播（broadcast）和矢量化（vectorization）。
# 广播和矢量化，是 NumPy 最精髓的特性，是 NumPy 的灵魂。所谓广播，就是将对数组的操作映射到每个数组元素上；矢量化可以理解为代码中没有显式的循环、索引等。NumPy数组最重要的特性是广播和矢量化，体现在性能上，就是接近C语言的运行效率，体现在代码上，则有这样的特点：
# 1、矢量化代码更简洁，更易于阅读；
# 2、代码行越少意味着出错的几率越小；
# 3、代码更接近于标准的数学符号;
# 4、矢量化代码更pythonic


