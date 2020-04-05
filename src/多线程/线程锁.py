# 比如多个线程都要对某个数据进行修改，则可能会出现不可预料的结果。为保证操作正确，就需要引入锁来进行线程间的同步。
# 对于某一时间只能让一个线程操作的语句放到 RLock的acquire 方法 和 release方法之间。即 acquire()方法相当于给RLock 锁  上锁，而 release() 相当于解锁
import threading,time
class MyThread1(threading.Thread):
    def run(self):
        global x
        lock.acquire() #上锁
        x+=10
        print("%s:%d"%(self.name,x))
        lock.release()

x=0
lock=threading.RLock() #创建可重用锁
def test():
    l=[]
    for i in range(5):
        l.append(MyThread1()) #创建5个线程，把他们放到一个list中
    for i in l:
        i.start()

test()

