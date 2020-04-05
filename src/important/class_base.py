# 在编写程序的时，不要对实例属性和类属性使用相同的名字，因为相同名称的实例属性将屏蔽掉类属性
# 但是当你删除实例属性后，再使用相同的名称，访问到的将是类属性。
class A:
    def hello(self):
        print("default")
    def hello(self,msg):  # python不支持方法重载，后者会覆盖前者方法
        print(msg)

a=A()
# a.hello() #会报错
#使用参数缺省值
class A:
    def hello(self, msg="default"):
        print(msg)

a = A()
a.hello()
a.hello("good")

# 方法重写
class A:
    def hello(self):
        print("i am A")

class B(A):  # 继承才会涉及方法重写
    def hello(self):
        print("i am B")

a = A()
a.hello()
b = B()
b.hello()

# 对于一个类来说，其成员可以分成两类，一类是实例成员，一类是类成员（也称为静态成员）。
# 实例成员是被每个对象拥有，静态成员被类拥有。
# 可以用@staticmethod修饰符来标记一个方法是静态方法(类方法)
class A:
    @staticmethod
    def fun1():
        pass
    def fun2(self):
        pass

a = A()
a.fun1()
a.fun2()
A.fun1()
# A.fun2() # 会报错，因为fun2是实例方法，无法被类直接调用，需要被类的实例（对象）调用。
# A.fun2(11) # 正确,函数中没有用到实例，传参无效，否则会报错
# 我们可以在实例方法中通过 self 或 类名 来调用静态方法。但在静态方法中却不能调用实例方法，因为静态方法中无法获取到对象本身，
# 除非我们自己给它加参数
# 直接在类中定义的变量是静态属性，在方法中（包括构造方法中）通过 self.变量名 定义的是实例属性
class A:
    name="class"
    def fun(self,name):
        self.name= name;

a = A()
print(a.name) # class
print(A.name) # class

a.fun("hello") 
print(a.name)  # hello
print(A.name)  # class
 
A.name = "newclass"
print(a.name)  # hello
print(A.name)  # newclass

# 对象的动态特点
# 在java，c++等非动态语言中，我们根据一个类创建了一个对象，这个对象拥有的成员（属性和方法）是固定不变的，就是类中定义的，对于属性，
# 区别只是不同对象有不同的值罢了。
# 在python这种动态语言中，创建的对象，还可以动态的绑定属性和方法。
# 我们在方法中 通过 self.变量名 就可以产生一个对象（实例）变量，而且这个定义可以在任意实例方法中
# 对象动态绑定只影响对象自己，不影响它所关联的类，和其它同一个类创建的对象。

def fun(self, info):
    print(self.msg + "," + info)
    
def fun1(info):
    print(info)

class A:
    pass

a = A()
a.msg = "dd"  # 动态绑定属性
a.test = fun    # 动态绑定方法
a.test1 = fun1    # 动态绑定方法

print(a.msg)
a.test(a, "good") # 可以将对象自己传给绑定的方法，让绑定的方法可以访问对象中的属性和其它方法
a.test1("good")

#__metaclass__=type  使用super方法python2.x版本需要加上这句，使用新式类
#__init__ 在类中类似这种前后双下划线的方法是魔法方法（特殊方法），会被python直接调用
#__init__ 是类的构造方法，是一个对象被创建就会被调用的方法
#__del__ 析构方法，在对象被垃圾回收前调用，但具体时间不可知

class A:
    def __init__(self,msg):
        self.msg=msg
    def hello(self):
        print(self.msg)
    def new(self):
        print("父类new")

class B(A):
    def __init__(self,othermsg,msg):  # 重写父类的构造方法
#         A.__init__(self, msg) #实例绑定到父类的构造方法，这就拥有父类的构造属性msg，父类的__init__方法需传参，子类也需要传对应参数（旧方法）
        super(B,self).__init__(msg) # 同上，两种方法调用父类构造 ，（新方法）
        self.othermsg=othermsg
    def show(self):
        print(self.othermsg)
    def new(self):  # 子类重写父类方法，多态
        print("子类new")

# b=B("hello","good")
# b.show()
# b.hello()
# a=A('11')
# b=B('22','33')
# a.new()
# b.new()

class ClassA(object):
    string1 = "这是一个字符串。"

    def instancefunc(self):
        print('这是一个实例方法。')
        print(self)

    @classmethod
    def classfunc(cls):
        print('这是一个类方法。')
        print(cls)

    @staticmethod
    def staticfun():
        print('这是一个静态方法。')


# test = ClassA() 
# test.instancefunc()  # 对象调用实例方法
# test.staticfun()  # 对象调用静态方法
# test.classfunc()  # 对象调用类方法
# print(test.string1)  # 对象调用类变量
# 
# ClassA.instancefunc(test)  # 类调用实例方法，需要带参数，这里的test是一个对象参数
# ClassA.instancefunc(ClassA)  # 类调用实例方法，需要带参数，这里的ClassA是一个类参数
# ClassA.staticfun()  # 类调用静态方法
# ClassA.classfunc()  # 类调用类方法
'''
记住以下两点就好了：
静态方法：无法访问类属性、实例属性，相当于一个相对独立的方法，跟类其实没什么关系，换个角度来讲，其实就是放在一个类的作用域里的函数而已。
类成员方法：可以访问类属性，无法访问实例属性。
'''

class Filter:
    def init(self):
        self.blocked=[]
    def filter(self,sequence):
        print([x for x in sequence if x not in self.blocked])


class SPAMFilter(Filter):
    def init(self):
        self.blocked=['SPAM']

f=Filter()
f.init()
f.filter([1,3,4])
s=SPAMFilter()
s.init()
s.filter([1,'SPAM',3.5,'张三','SPAM','AMS',4,55])
print(SPAMFilter.__bases__) # 返回已知类的基类们
print(Filter.__bases__)
print(isinstance(s,SPAMFilter))
print(isinstance(s,Filter))
print(isinstance(s,str))
print(isinstance(b'a', bytes)) # True
print(issubclass(SPAMFilter,Filter))
print(s.__class__)
print(type(s))
print(isinstance([1, 2, 3], (list, tuple))) # True # 判断一个变量是否是某些类型中的一种，判断是否是list或者tuple

#多个超类
class Calculator:
    def calculate(self,expression):
        self.value=eval(expression)
    def hello(self):
        print('cal hello')    
    
class Talk:
    def talk(self):
        print("hi,my value is",self.value)
    def hello(self):
        print('talk hello')     
        
class TalkingCalculator(Calculator,Talk): # 如果有同名方法，先继承的方法会重写后继承类中的方法
    pass

tc=TalkingCalculator()
tc.calculate("1+3*5")
tc.talk()
tc.hello() # cal hello 
print(hasattr(tc,'talk')) #检查方法是否已经存在
print(hasattr(getattr(tc,'talk'),'__call__') )#检查特性是否可调用

setattr(tc,'name','LP') #设置对象特性
print(tc.name)
print(tc.__dict__) #查看对象内所有存储的值



