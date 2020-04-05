# -*- coding:utf-8 -*-
'''
Created on 2020年1月7日

@author: pei.lu
'''

import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart

# 第一步： 连接到smtp服务器
smtp = smtplib.SMTP_SSL(host='smtp.163.com',port=465)

# 第二步：登录smtp服务器
smtp.login(user='邮箱账号',password='授权码')

# 第三步构建一封带附件的邮件
# 创建一封多组件的邮件
msg = MIMEMultipart()
# 添加发件人
msg['From'] = "xxxxx@163.com"
# 添加收件人
msg['To'] =  "xxx<xxxxx@qq.com>"
# 添加主题
msg['Subject'] = Header("带附件的测试邮件",charset='utf8')
# 添加邮件文本内容
# 创建邮件文件内容对象
text_content = MIMEText("这封邮件是用来测试发送是否成功的，邮件中添加了测试报告的附件",_charset='utf8')
# 把邮件的文本内容，添加到多组件的邮件中
msg.attach(text_content)

# 添加附件
f_msg = open('报告文件','rb').read()
app = MIMEApplication(f_msg)
app.add_header('content-disposition', 'attachment', filename='python.html')
msg.attach(app)

# 发送邮件
smtp.send_message(msg=msg,from_addr="发件人邮箱地址",to_addrs="收件人邮箱地址")