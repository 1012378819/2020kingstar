# unittset框架最核心的四个概念：
# TestCase：一个testcase的实例就是一个测试用例
# TestSuite：多个测试用例集合在一起。TestLoader:是用来把TestCase加载到TestSuite中的。
# TextTestRunner：用来执行测试用例的。
# fixture：测试用例环境的搭建和销毁，测试前准备环境的搭建（setUp）,执行测试代码（run），以及测试后环境的还原（tearDown）

import unittest

class Count:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def add(self):
        return self.a+self.b
    def sub(self):
        return self.a-self.b

class TestAdd(unittest.TestCase):    # 继承unittest.TestCase
    def test_add(self):
        j=Count(2,3)
        self.assertEqual(j.add(),5)
    def test_add2(self):
        j=Count(21,31)
        self.assertEqual(j.add(),52)

class TestSub(unittest.TestCase):
    def test_sub(self):
        j = Count(2, 3)
        self.assertEqual(j.sub(), -1)

    def test_sub2(self):
        j = Count(21, 31)
        self.assertEqual(j.sub(), -10)

# if __name__=="__main__":
#     unittest.main()
#构造测试集,这样可以选择测试部分case
suite= unittest.TestSuite()
suite.addTest(TestAdd("test_add"))
suite.addTest(TestAdd("test_add2"))
suite.addTest(TestSub("test_sub"))
suite.addTest(TestSub("test_sub2"))
test_dir= r"C:\Users\pei.lu.KINGSTAR\eclipse-workspace\new_2020\src\utest"
discover= unittest.defaultTestLoader.discover(test_dir, pattern='test.py')

#suite1=unittest.TestSuite(unittest_learn.makeSuite(TestAdd))
if __name__=="__name__":
    #运行测试集
    runner= unittest.TextTestRunner()
    runner.run(suite)
    # runner.run(suite1)
    # runner.run(discover)  #执行报错
