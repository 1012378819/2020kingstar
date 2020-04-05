# -*- coding: utf-8 -*-
"""
@time: 2020/3/8 22:06
@author: pei.lu
"""
import re
# re.match只匹配字符串的开始，如果字符串开始不符合正则表达式，则匹配失败，函数返回None；而re.search匹配整个字符串，直到找到一个匹配。

# Python 的 re 模块提供了re.sub用于替换字符串中的匹配项。
# re.sub(pattern, repl, string, count=0, flags=0)
# 参数：
# pattern : 正则中的模式字符串。
# repl : 替换的字符串，也可为一个函数。
# string : 要被查找替换的原始字符串。
# count : 模式匹配后替换的最大次数，默认 0 表示替换所有的匹配。

phone = "2004-959-559 # 这是一个国外电话号码"
num = re.sub(r'#.*$', "", phone) # 删除字符串中的 Python注释
print("电话号码是: ", num)  #  2004-959-559

num = re.sub(r'\D', "", phone) # 删除非数字(-)的字符串
print("电话号码是 : ", num) # 2004959559