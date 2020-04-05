# -*- coding: utf-8 -*-
"""
@time: 2020/3/3 13:34
@author: pei.lu
"""

# 示例：
import unittest
from HTMLTestRunnerNew import HTMLTestRunner
from file.openpyxl import ReadExcel  # file文件夹下的py文件中的ReadExcel类

class RegisterTestCase(unittest.TestCase):
    # 初始化测试用例
    def __init__(self, modethod_name, excepted, data):
        # modethod_name 测试用例方法名
        super().__init__(modethod_name)
        # excepted 测试用例的预期结果
        self.excepted = excepted
        # data 测试用例参数值
        self.data = data

    def setUp(self):
        print("准备测试环境，执行测试用例之前会执行此操作")

    def tearDown(self):
        print("还原测试环境，执行完测试用例之后会执行此操作")

    def test_register(self):
        res = register(*self.data)  # 没有此方法，只是举个例子
        try:
            self.assertEquals(self.excepted, res)
        except AssertionError as e:
            print("该条测试用例执行未通通过")
            raise e
        else:
            print("该条测试用例执行通过")

# 创建测试套件
suite = unittest.TestSuite()
# 调用封装好的读取数据的Excel类，获取测试数据
r1 = ReadExcel('cases.xlsx', 'Sheet1')  # 将调用封装好的Excel类
cases = r1.read_data_obj_new([2, 3])
# 将测试用例添加至测试套件中
for case in cases:
    # 需要使用eval()函数对except和data进行自动识别
    suite.addTest(RegisterTestCase('test_register', eval(case.excepted), eval(case.data)))
# 执行测试套件，生成测试报告
with open('report.html','w') as f:
    runner = HTMLTestRunner(stream=f,     # 需要写入的文件名
                            verbosity=2,  # 写入的等级，2是最高级的，也是最详细的
                            title ='python_test_rerport',  # 报告的名称
                            description='这是pytest单元测试的一份测试报告',  # 报告的相关描述
                            tester='WL')    # 测试者姓名
    runner.run(suite)

# 以下为示例：
import unittest
from pack.python13 import LoginTest
from pack import python13

# 创建一个测试集合
suite = unittest.TestSuite()

# 添加测试用例
# 第一种 单个用例添加：接收的参数是测试用例的对象
suite.addTest(LoginTest('test_login'))
suite.addTest(LoginTest('test_username_error'))
suite.addTest(LoginTest('test_password_lt6'))
# 第二种 一次添加多条测试用例
suite.addTests([LoginTest('test_login'), LoginTest('test_username_error'), LoginTest('test_password_lt6')])
# 第三种 一次添加一个测试用例类(类名不需要加引号)
loader = unittest.TestLoader()
suite.addTest(loader.loadTestsFromTestCase(LoginTest))  # 需要先将LoginTest类导进来
# 第四种 通过模块去添加
loader = unittest.TestLoader()
suite.addTest(loader.loadTestsFromModule(python13))

# 运行测试集合
# 创建一个runner对象
runner = unittest.TextTestRunner()
runner.run(suite)  # 执行测试套件

