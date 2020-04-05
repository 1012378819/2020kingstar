# -*- coding: utf-8 -*-
"""
@time: 2020/2/5 12:17
@author: pei.lu
"""
# 截屏
from PIL import ImageGrab
im=ImageGrab.grab((1300,500,1920,1080))
# im.show() # 调用系统默认的图像查看工具显示图像
im.save(r'C:\22code\demo.png') # 保存为文件

# 一行代码实现功能
# 1、把109张图片读到一个数组中
import numpy as np
from PIL import Image
try:
    data=np.stack([np.array(Image.open('head%d.png'%i)) for i in range(109)],axis=0)
except:
    print('没文件')
# 一行代码打印乘法口诀
# print('\n'.join([' '.join(["%2s *%2s = %2s"%(j,i,i*j) for j in range(1,i+1)]) for i in range(1,10)]))

# 一行代码打印迷宫
# print(''.join(__import__('random').choice('\u2571\u2572') for i in range(50*24)))

# 一行代码打印❤形
# print('\n'.join([''.join([('Love'[(x-y) %len('Love')] if ((x*0.05**2+(y*0.1)**2-1)**3-(x*0.05)**2*(y*0.1)**3) <=0 else ' ') for x in range(-30,30)]) for y in range(30,-30,-1)]))

# 一行代码打印分形图（小乌龟）
# print('\n'.join([''.join(['*' if abs((lambda a:lambda z,c,n:a(a,z,c,n))(lambda s,z,c,n:z if n==0 else s(s,z*z+c,c,n-1))(0,0.02*x+0.05j*y,40))<2 else ' ' for x in range(-80,20)]) for y in range(-20,20)]))

# print实现打字机效果

import time
def printer(text,delay=0.3):
    for ch in text:
        print(ch,end='',flush=True)
        time.sleep(delay)

# printer("sfsdf武汉热干面加油呀！")

def waiting(cycle=20,delay=0.5):    #  用python gzh_1.py  运行才能出效果
    """旋转式进度指示"""
    for i in range(cycle):
        for ch in ['-','\\','|','/']:  # 改为['--','\\','|','/']是另一个效果
            print('\b%s'%ch,end='',flush=True) # \b相当于键盘上的退格键，可以把刚刚打印过的最后一个字符擦掉重新打印
            time.sleep(delay)
# waiting()

def cover(cycle=50,delay=0.2):
    """覆盖式打印效果"""
    for i in range(cycle):
        s='\r%d'%i   # '\b'是回退一个字符，'\r'是退回到行首
        print(s.ljust(3),end='',flush=True) # ljust格式化输出用
        time.sleep(delay)

# cover()

# 避免浮点数计算误差，使得计算结果跟数学计算结果一致
from decimal import Decimal
a = 0.1
b = 0.2
c = float(Decimal(str(a)) + Decimal(str(b)))
# print(a+b,c)



