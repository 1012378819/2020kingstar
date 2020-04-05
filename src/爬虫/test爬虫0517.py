import requests
from pyquery import pyquery
import os

def get_html(url):
    # 请求网络，获取数据
    html = requests.get(url=url).content.decode('utf-8')
    py_html = pyquery(html)
    items = py_html('.span3').items()
    for each in items:
        src_img = each.find('img').attr('src')
        url_img_download = requests.get(src_img).content
        title_img = each.find('img').attr('title')
        print(title_img, src_img)
        with open('tony图/' + title_img + '.jpg', 'wb') as file:
            file.write(url_img_download)


file_path = os.path.join(os.getcwd(), 'tony图')
if not os.path.exists(file_path):
    os.makedirs(file_path)

url = "http://www.dbmeinv.com/?pager_offset=2"
get_html(url)