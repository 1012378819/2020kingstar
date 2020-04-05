# -*- coding:utf-8 -*-
#@time: 2019/11/22 14:47
#@author: pei.lu
from lemon_api.http_request import HttpRequest
import pandas as pd

df=pd.read_excel("test_data.xlsx")
test_data=df.values
print(test_data)
# for item in test_data:
#     print("目前正在执行的用例{0}：{1}".format(item[0],item[1]))
#     res=HttpRequest.http_request(item[2],eval(item[3]),item[4])
#     print('http执行的结果是{0}'.format(res))

#加入单元测试
#框架
#jenkins
#allure