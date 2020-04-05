# -*- coding: utf-8 -*-
"""
@time: 2020/2/6 16:59
@author: pei.lu
"""
# 荡秋千游戏(多线程)
# 创建10个子线程模拟小朋友荡秋千。规则：
#      1. 秋千上没有其他小朋友，才可以去玩，否则，只能等待
#      2. 每个小朋友只能玩一次，玩过之后就离开（线程结束）
#      3. 使用time.sleep()模拟荡秋千，时长1秒
#      4. 荡秋千开始和结束的时候，都要打招呼（print）
import threading
import time
lock=threading.Lock()
def play(name):
    if lock.acquire():
        print('%s开始荡秋千'%name)
        time.sleep(1)
        print('%s结束荡秋千' % name)
    lock.release()

def main():
    threads=list()
    for i in range(10):
        threads.append(threading.Thread(target=play,args=(chr(65+i),)))
        threads[-1].start()

    for i in threads:
        i.join()
    print('大家都玩过了，程序结束')
# if __name__ == '__main__':
#     main()

# 精度为1/100秒的计时器
import threading,sys

def f():
    print('0.00',end='')
    ct0=0.0
    t0=time.time()
    while True:
        ct=round(time.time()-t0,2)
        if ct!=ct0:
            ct0=ct
            print('\r%0.2f'%ct0,end='')
        time.sleep(0.01)

def timer():
    t = threading.Thread(target=f)
    t.setDaemon(True)
    print("请按回车键启动/停止计时器")
    t.start()
    input()

if __name__ == '__main__':
    timer() # 运行要通过python hw_2.py方式运行
