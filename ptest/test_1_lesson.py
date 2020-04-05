#!/usr/bin/python3
"""
@File    : first_lesson.py
@Time    : 2019/10/11 9:55
@Author  : 柠檬班-小简
@Email   : lemonban_simple@qq.com
@Company: 湖南省零檬信息技术有限公司
"""

# pip install pytest

def add(a,b):
    return a+b

# 用例：用例名称、前置条件、测试数据、步骤、断言(预期与实际的比对)、后置条件。
# 断言: 相等。 是否为成员、是否为真、是否包含、是否为空。。。
# assert 条件表达式(实际 == 预期   实际 in 预期) (表达式的结果为True或者False)
def test_add():
    # 步骤
    sum = add(100,200)
    # 断言
    assert sum == 300

# pytest特点：
# # 自动收集用例 ---
# 收集规则:
# # 确认目录(rootdir)-不能是python包: 在哪个目录下运行pytest，就从哪个目录下开始搜索
#   文件命名: test_*.py  或者  *_test.py
#   用例函数：函数名称以test_开头。
#            以Test开头的类(不包含__init__)，其下的以test_开头的函数。
# 运行方式
# 1、命令行运行：在目录下（非python包）执行直接命令pytest（见图）
# 2、文件运行：
# ·import pytest
# ·pytest.main()（就会找此文件所在的目录）
# ·pytest.main(["-s","-v"]) # 参数指定后可以看到pytest具体查找test文件的执行顺序

# 前置后置  -- unittest_learn、pytest（700+插件）
# 重运行机制
# 参数化
# allure报告
# 命令行传参


