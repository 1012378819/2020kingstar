# -*- coding: utf-8 -*-
"""
@time: 2020/2/24 11:13
@author: pei.lu
"""
# windons中的fork()-Process
from multiprocessing import Process
import time
def test(): #定义一个函数
    while True:
        print('-1-')
        time.sleep(1)
p = Process(target=test) #创建一个实例，就是一个新进程，并且执行的代码就是test()函数
p.start() #调用start方法让子进程开始运行。
p.join(10) #join表示延时时间，也就是等待子进程的时间，当10秒过了以后，则会运行主进程。
while True: #这里是主进程。
    print('-2-')
    time.sleep(1)

# Process实例
from multiprocessing import Process
import time

class Process_class(Process):  # 创建一个Process的子类。
    def run(self):  # 重写run方法，当调用start方法时，则会默认调用run方法，所以不用再填写target参数。
        while True:
            print('--1--')
            time.sleep(1)

p = Process_class()  # 实例化一个子进程。
p.start()  # 运行子进程
p.join(5)  # 这里将会等待子进程单独运行5秒。
while True:  # 主进程，当join等待结束父子进程一起运行。但是如果当父进程运行完，子进程还没有结束，那么父进程会继续等子进程。
    print('--main--')
    time.sleep(1)

# 进程池Pool
from multiprocessing import Pool  # 导入Pool模块类

def work(num):  # 创建一个进程的工作函数。
    for i in range(2):  # 表示每次工作需要执行2次。
        print('进程的pid是%d,进程值是%d' % (os.getpid(), num))  # 输出两次
        time.sleep(1)

p = Pool(2)  # 实例化对象，参数2表示创建2个子进程，就是说每次只能执行2个进程。

for i in range(6):
    print('--%d--' % i)
    p.apply_async(work, (i,))  # 向实例对象添加6次任务，就是6个进程，但是实例对象的进程池只有2个，需要每次执行2个进程，当2个进程执行完以后则会再次执行下面2个。

p.close()  # 关闭进程池，不再接收进程任务。
p.join()  # 当子进程工作结束后，则会运行主进程。

# Queue队列
# Process的Queue用法
from multiprocessing import Process, Queue  # 导入Process和Queue
import os, time

def write(q):  # 定义函数,接收Queue的实例参数
    for v in range(10):
        print('Put %s to Queue' % v)
        q.put(v)  # 添加数据到Queue
        time.sleep(1)

def read(q):  # 定义函数，接收Queue的实例参数
    while True:
        if not q.empty():  # 判断，如果Queue不为空则进行数据取出。
            v = q.get(True)  # 取出Queue中的数据，并返回保存。
            print('Get %s from Queue' % v)
            time.sleep(1)
        else:  # 如果Queue内没有数据则退出。
            break

if __name__ == '__main__':
    q = Queue()  # 实例化Queue括号内可选填，输入数字表示有多少个存储单位。以堵塞方式运行。必须等里边有空余位置时，才能放入数据，或者只能等里边有数据时才能取出数据，取不出数据，或者存不进数据的时候则会一直在等待状态。
    pw = Process(target=write, args=(q,))  # 实例化子进程pw,用来执行write函数，注意这里的函数不带括号，只是传递引用，参数需要使用args参数以元组的方式进行接收。
    pr = Process(target=read, args=(q,))
    pw.start()  # 开始执行pw。
    pr.start()  # 开始执行pr。
    pw.join()  # 等待pw结束
    pr.join()  # 等待pr结束
    print('Over')  # 主进程结束


