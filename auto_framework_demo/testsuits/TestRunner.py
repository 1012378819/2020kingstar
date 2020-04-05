import HTMLTestRunner
import os
import unittest
import time

report_path=os.path.dirname(os.path.abspath('.'))+'/test_report/'
now=time.strftime("%Y-%m-%d-%H-%M-%S",time.localtime(time.time()))
HtmlFile=report_path+now+'HTMLtemplate.html'
fp=file(HtmlFile,'wb')

suite=unittest.TestLoader().discover("testsuites")

if __name__=='__main__':
    runner=HTMLTestRunner.HTMLTestRunner(stream=fp,title='A项目测试报告',description='用例测试情况')
    runner.run(suite)

