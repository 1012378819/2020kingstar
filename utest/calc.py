#coding:utf-8
import unittest
import requests
import ddt

class MyTest(unittest.TestCase):
    def setUp(self):
        print("test case start")
    def tearDown(self):
        print("test case end")

# 测试一个接口时通常会编写多条case，而这些case除了传参不同外，其实并没什么区别。
# 这个时候就可以利用ddt来管理测试数据，提高代码复用率。
@ddt.ddt
class TestUnittest(MyTest):
    def test_1(self):
        print('test1 out')
    @ddt.data(('lp',14),('jc',10))
    @ddt.unpack
    def test_2(self,name,age):
        print(name,'is',age,'years old')

test_data = [{
    "clientCode": "韩",
    "topic": "测试接口",
    "content": "测试接口",
    "resrcType": "0",
    "assert": "200"   # assert并不是接口需要的参数，是为了对返回结果进行断言而加在这里的预期结果
},
    {
        "clientCode": "",
        "topic": "测试接口2",
        "content": "测试接口2",
        "resrcType": "0",
        "assert": "400"
    },
    {
        "clientCode": "韩",
        "topic": "",
        "content": "测试接口2",
        "resrcType": "0",
        "assert": "400"
    }]

@ddt.ddt
class Test(unittest.TestCase):
    def setUp(self):
        self.url='http://192.168.X.XXX:7001/XXX/api/XXXise/info/XXX/save.v'

    @ddt.data(*test_data)   # 一条用例，执行了3次，根据传参不同，得到不同的结果，相当于3条用例。
    def test_ddt(self,value):
        r=requests.post(self.url,value)
        print(r.json)
        self.assertTrue(value['assert'] in r.text)

if __name__ == '__main__':
    unittest.main()