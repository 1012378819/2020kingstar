import time
from selenium import webdriver
from test.logger import Logger

mylogger=Logger(logger='TestMyLog').getlog()
class TestMyLog:
    def print_log(self):
        driver=webdriver.Chrome()
        mylogger.info("打开浏览器")
        driver.maximize_window()
        mylogger.info("最大化浏览器窗口")
        driver.get("https://www.baidu.com")
        mylogger.info("打开百度首页")
        time.sleep(1)
        mylogger.info("暂停一秒")

testlog=TestMyLog()
testlog.print_log()