import threading
from queue import Queue

def job(data,q):
    for i in range(len(data)):
        data[i]=data[i]**2
    q.put(data) #put方法把结果放到队列

def exampleFunc():
    q=Queue() #新建一个队列

    threads=[] #新建一个空的多线程列表

    data=[[1,2,3],[2,3,4],[3,4,5],[4,5,6]]
    #for循环创建一个多线程，大小根据data[]的大小
    for x in range(4):
        t=threading.Thread(target=job,args=(data[x],q))
        t.start()
        threads.append(t)#把创建线程添加到多线程threads这个列表

    # for each_thread in threads:
    #     each_thread.join()

    results=[]

    for  y in range(4):
        results.append(q.get())#q.get()是从队列取出结果

    print(results)

# exampleFunc()

# 通过继承 thread.Thread 类 来创建线程
import threading,time

class MyThread(threading.Thread):
    def run(self):  #需要重载 threading.Thread 类的 run 方法，然后调用 start()开启线程就可以了
        time.sleep(2)
        print('my thread over')

def test1():
    ma=MyThread()
    print(ma.is_alive()) #这个方法用于判断线程是否运行。当线程未调用start()来开启时返回False
    ma.start()
    print(ma.is_alive())
    time.sleep(3)
    print(ma.is_alive())#线程已经执行后并结束时，isAlive()也会返回False

def test2():
    ta=MyThread()
    ta.daemon=True #daemon属性用来设置线程是否随主线程退出而退出,默认否
    ta.start()
    #ta.join() 可以加这个测试join的功能
    print('main thread over')

test2()