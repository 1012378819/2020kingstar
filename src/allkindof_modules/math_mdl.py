# -*- coding: utf-8 -*-
"""
@time: 2020/2/21 15:27
@author: pei.lu
"""
# 在math模块中，提供了另外几种将浮点数截断成小数的方法，分别是trunc截断、floor向下取整、ceil向上取整。
# round函数，如果不传入第2个参数，也有取整的功能

# 导入math
import math
a = 3.556
b = -3.556
# 直接截断
math.trunc(a) # 3
math.trunc(b) # -3
# 向下取整
math.floor(a) # 3
math.floor(b) # -4
# 向上取整
math.ceil(a) # 4
math.ceil(b) # -3
# 四舍五入取整
round(a) # 4
round(b) # -4

print(math.__dict__)
print(math.__doc__)