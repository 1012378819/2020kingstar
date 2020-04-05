# -*- coding: utf-8 -*-
"""
@time: 2020/2/20 11:07
@author: pei.lu
"""
# pandas是一个数据处理的包，本身提供了许多读取文件的函数，像read_csv（读取csv文件），read_excel（读取excel文件）等
import pandas as pd
# 1 读excel
df=pd.read_excel(r'excel_dxtest.xlsx',sheet_name=1)
# print(df.head())
# 2 写excel
from pandas import DataFrame
data={'name':['张三','李四','王五'],'age':[11,22,33],'sex':['男','女','男']}
df=DataFrame(data)
df.to_excel('pandas_new.xlsx')
# todo 待安装openxlsx模块后测试