# -*- coding:utf-8 -*-
'''
Created on 2020年1月7日

@author: pei.lu
'''
# 待获取的目标数据 (职位名称\薪资范围\所属公司)
import requests
from lxml import etree

s = requests.session()
header = {
    "cookie":"_uab_collina=156013238928273573152563; lastCity=101010100; __c=1576727614; __g=-; Hm_lvt_194df3105ad7148dcf2b98a91b5e727a=1576727614; Hm_lpvt_194df3105ad7148dcf2b98a91b5e727a=1576727614; __l=l=%2Fwww.zhipin.com%2F%3Fka%3Dheader-home-logo%26city%3D101010100&r=https%3A%2F%2Fwww.zhipin.com%2F%3Fka%3Dheader-home-logo&friend_source=0&friend_source=0; __a=12875726.1576727614..1576727614.2.1.2.2; __zp_stoken__=d78eVjuAQ37e1fHI1t6xEr7uLmzoPWCALMYtdQ%2Fk59lWJaxYFJnngZe64gxX529QtBuD3y4nmrjnnAYCmBn98W3jznBL%2BPb02LVrGXjyqcKWtU7k%2BxcdENjUJKQiEEjEiL2R",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.80 Safari/537.36",
}

# 目标网站的地址
url = "https://www.zhipin.com/c101010100/?query=%E8%87%AA%E5%8A%A8%E5%8C%96%E6%B5%8B%E8%AF%95&ka=sel-city-101010100"

# 发送请求，获取页面内容
response = s.get(url=url, headers=header)

# 获取页面内容（代码）
html_str = response.content.decode('utf8')
print(html_str)

# 转换
html = etree.HTML(html_str)

# 提取目标数据（招聘岗位）

# job_list = html.xpath('//*[@id="main"]/div/div[3]/ul/li')

# 提取所有的岗位节点
job_list = html.xpath('//div[@class="job-list"]/ul/li')
print(job_list)

for job in job_list:
    # 获取岗位名称
    job_name = job.xpath('.//div[@class="job-title"]/text()')
    # 获取薪资待遇
    price = job.xpath('.//span[@class="red"]/text()')
    # 获取公司名称
    job_company = job.xpath('.//div[@class="company-text"]/h3/a/text()')

    # 格式化一下数据
    job_data = '岗位名称：{}  薪资：{}  公司：{}'.format(job_name[0], price[0], job_company[0])
    print(job_data)