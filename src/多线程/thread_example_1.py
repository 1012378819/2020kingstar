# -*- coding:utf-8 -*-
'''
Created on 2020年1月5日

@author: pei.lu
'''
# python的多线程是并发（多个任务对于1个CPU，线程快速切换），不是并行的
# “全局解释器锁” 控制一个时刻只有一个线程可以执行python代码，所以线程实际是并发，没发并行的，也就是伪多线程
# 多进程可以并行，实现真正的多线程
# python中多线程是可以共享全局变量的，但会造成资源竞争
# 解决资源竞争问题：1、加锁   2、队列
import threading,time

def work1(name,age):
    for i in range(6):
        time.sleep(1)
        print('{}这在浇花，她年龄{}'.format(name,age))

def work2(name,age):
    for i in range(4):
        time.sleep(1)
        print('{}这在打墙，她年龄{}'.format(name,age))

# 创建两个线程，分别做这两件事
# 使用threading模块中的Thread类来创建线程对象，通过target参数去指定该线程的工作任务
# 两种传参方式
t1=threading.Thread(target=work1,args=('xiaomi',16))
t2=threading.Thread(target=work2,kwargs={'age':10,'name':'zhangsan'})

s_time=time.time()
# 启动线程
t1.start()
t2.start()
# join不传参数，让主线程等待子线程执行完
# t1.join()
# t2.join()
# join传参数，让主线程等待子线程执行一个固定的事件
t1.join(2)
t2.join(1)
e_time=time.time()
print('总执行时间：',e_time-s_time)

def example1():
    print(threading.active_count()) #计算当前一共有多少个激活的线程
    print(threading.enumerate()) #第二个方法是显示激活线程是那些
    adder_thread=threading.Thread(target=thread_job)
    adder_thread.start()
    print(threading.active_count())  # 计算当前一共有多少个激活的线程
    print(threading.enumerate())  # 第二个方法是显示激活线程是那些

def thread_job():
    print('%s' %threading.current_thread())

def thread_job1():
    print('start\n')
    for i in range(4):
        time.sleep(0.5)
    print('finish')

def example2():
    thread1=threading.Thread(target=thread_job1,name='T1')
    thread1.start()
    thread1.join() # 主线程等待thread1线程结束才继续执行,注释掉此句 主线程就会继续执行下去打印all finished
    print('all finished!\n')

# example1()
# example2()