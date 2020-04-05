#coding:utf-8
# from __builtin__ import file
# from HTMLTestRunner import HTMLTestRunner
from email.mime.text import MIMEText
import smtplib, time,os
import unittest

#定义发送邮件
def send_mail(file_new):
    f=open(file_new,'rb')
    mail_body=f.read()
    f.close()
    msg=MIMEText(mail_body,'html','utf-8')
    msg['Subject']=u'自动化测试报告'
    smtp=smtplib.SMTP()
    smtp.connect('smtp.126.com')
    smtp.login('send@126.com','123456')
    smtp.sendmail('send@126.com','receiver@126.com',msg.as_string())
    smtp.quit()
    print('email has send out!')

def new_report(testreport):
    lists=os.listdir(testreport)
    lists.sort(key=lambda fn: os.path.getmtime(testreport+"\\"+fn))
    file_new=os.path.join(testreport,lists[-1])
    return file_new

if __name__=="__main__":
    discover= unittest.defaultTestLoader.discover('./test_case', pattern='test*.py')
    now= time.strftime("%Y-%m-%d_%H_%M_%S")
    filename='./report/'+now+'result.html'
    fp=open(filename,'wb')
    runner=HTMLTestRunner(stream=fp,title=u'测试报告',description=u'用例执行情况：')
    runner.run(discover)
    fp.close()
    newreport=new_report('./report/')
    send_mail(newreport) #发送测试报告