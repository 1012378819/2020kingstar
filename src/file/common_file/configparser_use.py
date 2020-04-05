# -*- coding: utf-8 -*-
"""
@time: 2020/2/29 18:30
@author: pei.lu
"""
# ConfigParser在python中用来读取ini类型的配置文件的
import configparser
import os
cf=configparser.ConfigParser()
f=os.getcwd()+'\data_files\config.ini'
cf.read(f,encoding='utf-8')
# 获取文件内容
print(cf.sections()) # 返回所有的section
print(cf.options('server')) # 返回section所有的options
print(cf.items('server')) # 返回section所有键值对
for k,v in cf.items('server'):
    print('{}:{}'.format(k,v))
print(cf.get('database','dbuser')) # 返回section中option的值
print(cf.get('database','instance',fallback='instance不存在')) # 若section或option不存在，fallback返回后备值
print('server' in cf)
print(cf['database']['dbname'] )


# 写新配置到文件
section='login'
print(cf.has_section('login'))
print(cf.has_option('login', 'pwd'))
if not cf.has_section(section):
    cf.add_section(section) # 添加一个section节点
    cf.set(section,'user','3457') # 设置section节点中键名、键值
    cf.set(section,'password','yishuichuxia') # 设置section节点中键名、键值
cf.set(section, 'user', '1234')  # 修改，覆盖之前的值
# cf.remove_section(section)       # 删除
cf.remove_option('database','useless')  # 删除
cf["default"] = {'ServerAliveInterval': '45',       # 新增
                      'Compression': 'yes',
                     'CompressionLevel': '9',
                     'ForwardX11':'yes'
                     }
with open(f,'w') as config_file:
    cf.write(config_file) # 新增修改删除都需要写入('w')配置文件