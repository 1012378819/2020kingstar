# -*- coding: utf-8 -*-
"""
@time: 2020/2/8 18:03
@author: pei.lu
"""
import time
#
# print('   :<---', end='\r')
# for i in range(1, 30):
#     print(str(i), end='\r')
#     time.sleep(.2)
# print('100:OK!!')
import time
for i in range(11):
    time.sleep(0.5)
    print('\r当前进度：{0}{1}%'.format('▉'*i,(i*10)), end='')
print('加载完成！')