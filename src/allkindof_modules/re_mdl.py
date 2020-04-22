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

def test_1():
    a='fs1fj24%%^^!@%#E88R—+=G5f_er__ge^%@895'
    pattern=re.compile("\D+")   # 匹配字母下划线特殊字符（除数字外地）>=1位
    pattern1=re.compile("\d+")  # 匹配数字>=1位
    pattern2=re.compile("\W+")  # 匹配特殊字符（除字母数字下划线外的）>=1位
    pattern3=re.compile("\w+")  # 匹配字母数字下划线>=1位
    pattern4=re.compile(".")  # 匹配1位数
    pattern5=re.compile(".*")  # 匹配>0位数
    pattern6=re.compile(".+")  # 匹配>=1位数,不加？号贪婪模式
    print(pattern.findall(a))
    print(pattern1.findall(a))
    print(pattern2.findall(a))
    print(pattern3.findall(a))
    print(pattern4.findall(a))
    print(pattern5.findall(a))
    print(pattern6.findall(a))

# test_1()

a='1452480842@qq.com'
pattern=re.compile("(\w*)\.com")   # . *特殊字符要转义
pattern1=re.compile("145(\w*\W\w+?)\.com")   # . *特殊字符要转义
pattern2=re.compile("(\w+@\w+\.com)")   # 邮箱的匹配规则
pattern3=re.compile("(\w+\W\w+\.com)")   # 邮箱的匹配规则
pattern4=re.compile("(\w+\W(\w+)\.com)")   # 匹配邮箱的qq,多个()返回多个值
pattern5=re.compile("(\w+)\W\w+\.com")   # 匹配邮箱的数字
print(pattern.findall(a))
print(pattern1.findall(a))
print(pattern2.findall(a))
print(pattern3.findall(a))
print(pattern4.findall(a))
print(pattern5.findall(a))

# 匹配数字\d,匹配字母或数字\w,匹配所有乱七八糟的符号.,另外. *特殊字符要转义
