#跑马灯
import time,os
content="浙江温州，最大皮革厂倒闭，全场2折，欢迎选购！"
# while True:
#     os.system('clear')
#     print(content)
#     time.sleep(0.2)
#     content=content[1:]+content[0]


# 一球从100米高度自由落下，每次落地后反跳回原高度的一半；再落下，求它在第10次落地时，共经过多少米？第10次反弹多高？

import math
for i in range(100,200):
    for j in range(2,round(math.sqrt(i))+1):
        if i%j==0:
            break
    else:
        print("".format())