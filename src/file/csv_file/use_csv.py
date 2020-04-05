# -*- coding:utf-8 -*-
# @Time : 2020/4/4 23:31
# @Author: lup
__author__ = 'pei.lu'

# csv是文本文件，无需导入任何模块

grade=[
    {'name':'zangsan','python':100,'java':90,'C++':60},
    {'name':'wangwu','python':70,'java':60,'C++':60},
    {'name':'lp','python':100,'java':100,'C++':100},
       ]

# 写 csv文件
with open(r'.\grade.csv','w') as fp:
    fp.write('NAME,PYTHON,JAVA,C++\n')
    for item in grade:
        fp.write('%s,%d,%d,%d\n'%(item['name'],item['python'],item['java'],item['C++']))

# 读 csv文件
result=list()
with open(r'd:\grade.csv','r') as fp:
    lines=fp.readlines()
    col_names=lines[0].strip().split(',')
    for line in lines[1:]:
        result.append(dict(zip(col_names,line.strip().split(','))))

print(result)