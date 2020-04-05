#!/usr/lib/python
# -*- coding: utf-8 -*-
import json, urllib
from urllib import urlencode

# ----------------------------------
# 老黄历调用示例代码 － 聚合数据
# 在线接口文档：http://www.juhe.cn/docs/65
# ----------------------------------

def main():
    # 配置您申请的APPKey
    appkey = "*********************"

    # 1.日历
    request1(appkey, "GET")

    # 2.时辰
    request2(appkey, "GET")


# 日历
def request1(appkey, m="GET"):
    url = "http://v.juhe.cn/laohuangli/d"
    params = {
        "key": appkey,  # 应用APPKEY(应用详细页查询)
        "date": "",  # 日期，格式2014-09-09

    }
    params = urlencode(params)
    if m == "GET":
        f = urllib.urlopen("%s?%s" % (url, params))
    else:
        f = urllib.urlopen(url, params)

    content = f.read()
    res = json.loads(content)
    if res:
        error_code = res["error_code"]
        if error_code == 0:
            # 成功请求
            print(res["result"])
        else:
            print("%s:%s" % (res["error_code"], res["reason"]))

    else:
        print("request api error")


# 时辰
def request2(appkey, m="GET"):
    url = "http://v.juhe.cn/laohuangli/h"
    params = {
        "key": appkey,  # 应用APPKEY(应用详细页查询)
        "date": "",  # 日期，格式2014-09-09

    }
    params = urlencode(params)
    if m == "GET":
        f = urllib.urlopen("%s?%s" % (url, params))
    else:
        f = urllib.urlopen(url, params)

    content = f.read()
    res = json.loads(content)
    if res:
        error_code = res["error_code"]
        if error_code == 0:
            # 成功请求
            print(res["result"])

        else:
            print("%s:%s" % (res["error_code"], res["reason"]))

    else:
        print("request api error")



if __name__ == '__main__':
    main()