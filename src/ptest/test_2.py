#!/usr/bin/python3
"""
@File    : test_2.py
@Time    : 2019/10/11 10:23
@Author  : 柠檬班-小简
@Email   : lemonban_simple@qq.com
@Company: 湖南省零檬信息技术有限公司
"""

def sub(a,b):
    return a-b

class TestPytest:
    def test_sub2(self):
        s = sub(333.33,33)
        assert s == 100.33

    def cc(self):
        print("pytest")

def test_sub():
    print(11)
    s = sub(333,33)
    assert s == 300


