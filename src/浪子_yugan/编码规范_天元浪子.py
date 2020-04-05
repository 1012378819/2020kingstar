# -*- coding: utf-8 -*-
#@time: 2019/11/29 15:04
#@author: pei.lu

"""通常这里是关于本文档的说明（docstring），须以半角的句号、 问号或惊叹号结尾!

本行之前应当空一行，继续完成关于本文档的说明
如果文档说明可以在一行内结束，结尾的三个双引号不需要换行；否则，就要像下面这样
"""

import os, time
import datetime
import math

import numpy as np
import xlrd, xlwt, xlutils

# import youth_mongodb
# import youth_curl

BASE_PATH = r"d:\YouthGit"
LOG_FILE = u"运行日志.txt"


class GameRoom(object):
    """对局室"""

    def __init__(self, name, limit=100, **kwds):
        """构造函数!

        name        对局室名字
        limit       人数上限
        kwds        参数字典
        """

        pass


def craete_and_start():
    """创建并启动对局室"""

    pass


if __name__ == '__main__':
    # 开启游戏服务
    start()

# 比较重要的注释段, 使用多个等号隔开, 可以更加醒目, 突出重要性,如下

# =====================================
# 请勿在此处倾倒垃圾!!!
# =====================================

# 命名规范
#
# 模块尽量使用小写命名，首字母保持小写，尽量不要用下划线
# 类名使用驼峰(CamelCase)命名风格，首字母大写，私有类可用一个下划线开头
# 函数名一律小写，如有多个单词，用下划线隔开
# 私有函数可用一个下划线开头
# 变量名尽量小写, 如有多个单词，用下划线隔开
# 常量采用全大写，如有多个单词，使用下划线隔开
# ———————————————
