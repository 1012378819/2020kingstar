# 条件变量表示当线程满足某一个 条件才被唤醒，否则一直阻塞
#
# 对比 只用锁不用条件变量 的好处就是：只用锁的话，如果一个线程在上锁后，解锁前，因为某一条件一直阻塞着，那么锁就一直解不开，
# 那么其他线程也就因为一直获取不了锁而跟着阻塞着，这样效率就不好，浪费了很多时间。对于这种情况，锁+条件变量可以让该线程先 解锁，
# 然后阻塞着，等待条件满足了，再重新唤醒并获取锁(上锁)。这样就不会因为一个线程阻塞着而影响其他线程也跟着阻塞了。
# Condition 提供的方法：
# acquire() 和 release() 表示上锁和解锁，和 单纯的锁机制一样。
# wait()  解开锁，阻塞，直到其他线程调用了notify()或者notifyAll才被唤醒，注意，这里的wait()跟上面Event提到的wait()不是同一样东西
# notify() 发出资源可用的信号，唤醒任意一条因 wait(）阻塞的进程
# notifyAll() 发出资源可用信号，唤醒所有因wait()阻塞的进程

#实例：一家蛋糕店：只会做一个蛋糕，卖出后才会再做一个。绝对不会做积累到2个蛋糕
import threading,time
class Server(threading.Thread):
    def run(self):
        global x
        while True:
            con.acquire()
            while x>0:
                con.wait()
            x+=1
            time.sleep(1)
            print(self.name,':I make %d cake!'%(x))
            con.notifyAll()
            con.release()

class Client(threading.Thread):
    def run(self):
        global x
        con.acquire()
        while x==0:
            con.wait()
        x-=1
        print(self.name,'I bought a cake!the rest is %d cake'%(x))
        con.notifyAll()
        con.release()

def test():
    ser=Server()
    ser.name='Cake Server'
    client=[]
    for i in range(3):
        client.append(Client())
    ser.start()
    for c in client:
        c.start()

x=0
con=threading.Condition()
test()
