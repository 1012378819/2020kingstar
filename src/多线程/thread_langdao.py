# -*- coding: utf-8 -*-
"""
@time: 2020/2/6 17:00
@author: pei.lu
"""
## demo 创建并使用线程
# 你（主线程）启动3个子线程，名字分别是A、B、C。其中A线程启动后，你要先观察5秒钟，再启动其他线程。
# 每个子线程的任务是每隔指定时间间隔就向你问好，并报上自己的名字，你呢，只管睡觉。15秒后，你醒了。
# 你逐一检查了各个子线程的工作状态之后，结束运行
## demo1 线程同步---3.1 线程锁 Lock
# 前几天，我想在一个几百人的微信群里统计喜欢吃苹果的人数。有人说，咱大家从1开始报数吧，并敲了起始数字1，
# 立马有人敲了数字2，3。但是统计很快就进行不下去了，因为大家发现，有好几个人敲4，有更多的人敲5。
# 这就是典型的资源竞争冲突：统计用的计数器就是唯一的资源，很多人（子线程）都想取得写计数器的资格。怎么办呢？
# Lock（互斥锁）就是一个很好的解决方案。Lock只能有一个线程获取，获取该锁的线程才能执行，否则阻塞；执行完任务后，
# 必须释放锁。
## 3.3 事件Event
# 想象我们每天早上上班的场景：为了不迟到，总得提前几分钟（我一般都会提前30分钟）到办公室，打卡之后，一看表，
# 还不到工作时间，大家就看看新闻、聊聊天啥的；工作时间一到，立马开工。如果有人迟到了呢，自然就不能看新闻聊天了，
# 得立即投入工作中。这个场景中，每个人代表一个线程，工作时间到，表示事件(Event)发生。事件发生前，线程会调用
# wait() 方法阻塞自己（对应看新闻聊天），一旦事件发生，会唤醒所有调用 wait() 而进入阻塞状态的线程
# 3.4 条件 Condition
# 两位小朋友，Hider 和 Seeker，打算玩一个捉迷藏的游戏，规则是这样的：Seeker 先找个眼罩把眼蒙住，喊一声“我已经蒙上眼了”；
# 听到消息后，Hider 就找地方藏起来，藏好以后，也要喊一声“我藏好了，你来找我吧”；Seeker 听到后，也要回应一声“我来了”，
# 捉迷藏正式开始。各自随机等了一段时间后，两位小朋友都憋住了跑了出来。谁先跑出来，就算谁输
import random
import time
import threading
def hello(name,t):
    """线程函数"""
    for i in range(10):
        print('hello,i am %s'%name)
        time.sleep(t)
def demo():
    A=threading.Thread(target=hello,args=('A',1),name='A')
    B=threading.Thread(target=hello,args=('B',2),name='B')
    C=threading.Thread(target=hello,args=('C',3),name='C')

    # 如何令子线程在主线程结束时无条件跟随主线程一起走人呢？很简单，在线程 start() 之前，使用 setDaemon(True) 设置该线程为守护线程就可以了。子线程的 daemon 属性默认为 False。
    C.setDaemon(True) # 设置子线程在主线程结束时是否无条件一起退出

    A.start()
    A.join(5) # 等待A线程结束，若超过5s未结束，代码继续
    B.start()
    C.start()
    time.sleep(15)
    print('A%s'%('still in work' if A.isAlive() else 'finish'))
    print('B%s'%('still in work' if B.isAlive() else 'finish'))
    print('C%s'%('still in work' if C.isAlive() else 'finish'))
    print('主线程下班了')

lock=threading.Lock() # 创建互斥锁
counter=0 # 计数器
def hello1():
    global counter

    if lock.acquire(): # 请求互斥锁，如果被占用，则阻塞，直至获取到锁
        time.sleep(0.2) # 假装思考写要0.2s
        counter+=1
        print('我是第%d个'%counter)

    lock.release() # 释放锁，不能忘！！
# Lock
def demo1():
    threads=list()
    for i in range(10): # 假设群里有10人喜欢吃苹果
        threads.append(threading.Thread(target=hello1))
        threads[-1].start()

    for t in threads:
        t.join()

    print('统计完毕，共%d人'%counter)

E=threading.Event() # 创建事件
def work(id):
    print('<%d号员工>上班打卡'%id)
    if E.is_set(): # 已经到点了
        print('<%d号员工>迟到了'%id)
    else: # 还不到点
        print('<%d号员工>浏览网页中。。。' % id)
        E.wait() # 等上班时间到

    print('<%d号员工>开始工作了。。。' % id)
    time.sleep(10) # 工作10s后下班了
    print('<%d号员工>下班了' % id)
# Event
def demo2():
    E.clear() # 设置为“未到上班时间”
    threads=list()
    for i in range(3):
        threads.append(threading.Thread(target=work,args=(i,)))
        threads[-1].start()
    time.sleep(5) # 5s后上班时间到
    E.set()
    time.sleep(5) # 5s后，大佬（9号）到
    threads.append(threading.Thread(target=work, args=(9,)))
    threads[-1].start()

    for t in threads:
        t.join()

    print('都下班了，关灯关门走人')

# event 实例管理着一个内部标志，通过 set() 方法来将该标志设置成 True，使用 clear() 方法将该标志重置成 False
# wait() 方法会使当前线程阻塞直到标志被设置成 True，wait()可以选择给他一个参数，代表时间，代表阻塞多长时间，若不设置就是阻塞直到标志被设置为True
# isSet()方法：能判断标志位是否被设置为True
import threading,time
class Mon(threading.Thread):
    def run(self):
        Dinner.clear()
        print('cooking dinner')
        time.sleep(0.02)
        Dinner.set()
        print(self.name,':dinner is OK!')
class Son(threading.Thread):
    def run(self):
        while True:
            if Dinner.isSet():
                break
            else:
                print('dinner isnot ready!')
        print(self.name,':Eating dinner')

def test():
    mon=Mon()
    son=Son()
    mon.name='Mon' #给线程命名，否则默认从1开始递增thread-1
    son.name='Son'
    mon.start()
    son.start()

Dinner=threading.Event()
test()


cond=threading.Condition() # 创建条件对象
draw_Seeker=False # Seeker小朋友认输
draw_Hidwer=False # hider小朋友认输
def seeker():
    """Seeker小朋友的线程函数"""
    global draw_Hidwer,draw_Seeker
    time.sleep(1) # 确保Hider小朋友已经进入消息等待状态
    cond.acquire() # 阻塞时请求资源
    time.sleep(random.random()) # 假装蒙眼需要花费时间
    print('Seeker: 我已经蒙上眼了')
    cond.notify() # 把消息通知到Hider小朋友
    cond.wait() # 释放资源并等待Hider小朋友已经藏好的消息
    print('Seeker: 我来了') # 收到Hider小朋友已经藏好的消息后
    cond.notify() # 把消息通知到Hider小朋友
    cond.release() # 不要再听消息了，彻底释放资源
    time.sleep(random.randint(3,10)) # Seeker小朋友的耐心只有3-10秒钟

    if draw_Hidwer:
        print('Seeker: 哈哈，我找到你了，我赢了')
    else:
        draw_Seeker = True
        print('Seeker: 算了，我找不到你，我认输啦')

def hider():
    """Hider小朋友的线程函数"""
    global draw_Seeker,draw_Hidwer
    cond.acquire() # 阻塞时请求资源
    cond.wait() # 如果先于Seeker小朋友请求到资源，则立刻释放并等待
    time.sleep(random.random()) # 假装找地方躲藏需要花费时间
    print('Hider: 我藏好了，你来找我吧')
    cond.notify() # 把消息通知到Seeker小朋友
    cond.wait() # 释放资源并等待Seeker小朋友开始找人的消息
    cond.release() # 不要再听消息了，彻底释放资源
    time.sleep(random.randint(3,10)) # Hider小朋友的耐心只有3-10秒钟

    if draw_Seeker:
        print('Hider: 哈哈，你没找到我，我赢了')
    else:
        draw_Hidwer = True
        print('Hider: 算了，这里太闷了，我认输，自己出来吧')
def demo3():
    th_seeker=threading.Thread(target=seeker)
    th_hider=threading.Thread(target=hider)
    th_seeker.start()
    th_hider.start()
    th_seeker.join()
    th_hider.join()
if __name__ == '__main__':
    # demo()
    # demo1()
    # demo2()
    demo3()



