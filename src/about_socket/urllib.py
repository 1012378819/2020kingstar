#urllib模块可以在给出数据源的url时让从不同服务器读取和下载数据，常应用来做爬虫技术
import urllib.request

webpage=urllib.request.urlopen('http://www.baidu.com')

text=webpage.read() #读取全部
print(text)
urllib.request.urlretrieve('http://www.python.org','C:\\python_webpage.html')#获取python主页并存储在文件C:\python_webpage.html中

