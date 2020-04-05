# -*- coding: utf-8 -*-
"""
@time: 2020/3/15 13:10
@author: pei.lu
"""
# 有了线程技术，我们就可以在一个进程中创建多个线程，让它们在“同一时刻”分别去做不同的工作了。
# 这些线程共享同一块内存，线程之间可以共享对象、资源，如果有冲突或需要协同，还可以随时沟通以解决冲突或保持同步。
# 但有一个致命的缺点：在一个进程内，不管你创建了多少线程，它们总是被限定在一颗CPU内，或者多核CPU的一个核内。so，多线程编程无法充分发挥多核计算资源的优势
# 多进程技术正好弥补了多线程编程的不足，我们可以在每一颗CPU上，或者多核CPU的每一个核上启动一个进程，如果有必要，还可以在每个进程内再创建适量的线程，最大限度地使用计算资源解决问题。
# 因为不在同一块内存区域内，和线程相比，进程间的资源共享、通讯、同步等，都要麻烦的多，收到的限制也更多
# multiprocessing 模块引入了在 threading 模块中没有的API，比如进程池（Pool）、共享内存（Array 和 Value）等

# https://mp.weixin.qq.com/s/U7bWJJiWGdis8zCm_yco1Q
# 演示典型的生产者——消费者模式：进程A负责往地上扔钱，进程B负责从地上捡钱。
import os,time,random
import multiprocessing as mp

def sub_process_A(q):
    """A进程函数：生成数据"""
    while True:
        time.sleep(2*random.random())
        q.put(random.randint(10,100)) # put()和get()两个方法均默认为阻塞式，一旦队列满，put()被阻塞

def sub_process_B(q):
    """B进程函数：使用数据"""
    words=['哈哈，','天哪','卖狗的！','填上掉馅饼了？']
    while True:
        print('%s捡到了%d块钱'%(words[random.randint(0,3)],q.get())) # 一旦队列空，get()被阻塞

if __name__ == '__main__':   # todo 不懂子进程为什么没有输出
    print('主进程（%s）开始，按任意键结束'%os.getpid())
    q=mp.Queue(10)
    p_a=mp.Process(target=sub_process_A,args=(q,))
    p_a.daemon=True
    p_a.start()
    p_b=mp.Process(target=sub_process_B,args=(q,))
    p_b.daemon=True #  若daemon 设置为 False，则主进程结束后，子进程不会随之结束，从而成为僵尸进程
    p_b.start()

    input()
