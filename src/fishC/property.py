class Rectangle:
    def __init__(self):
        self.width=0
        self.height=0
    def setSize(self,size):
        self.width,self.height=size
    def getSize(self):
        return self.width,self.height
    size=property(getSize,setSize)  # property的4个参数分别叫做fget、fset、fdel、doc

r=Rectangle()
r.width=10
r.height=5
print(r.getSize())
r.setSize((150,100))
print(r.width)

class Rectangle1():
    def __init__(self):
        self.width=0
        self.height=0
    def __setattr__(self, name, value):  # 在所涉及的特性不是size时也会被调用
        if name=='size':
            self.width,self.height=value
        else:
            self.__dict__[name]=value  # 用来替代普通的特性赋值
    def __getattr__(self, name): # 此方法只在普通特性没有被找到的时候调用
        if name=='size':
            return self.width,self.height
        else:
            raise AttributeError

r1=Rectangle1()
print(r1.height,r1.width)
r1.size=((100,50))
print(r1.size)
r1.age=15
print(r1.age)
print(r1.__dict__)
