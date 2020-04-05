# -*- coding:utf-8 -*-
'''
Created on 2019年12月22日

@author: pei.lu
'''
import os
print(os.getcwd())
print(os.name)
print(os.curdir)  # .
print(os.pardir)  # ..
print(os.listdir(os.curdir))
print(os.listdir('.'))
print([d for d in os.listdir('.')]) # os.listdir可以列出文件和目录
# os.system('cmd') # ？
# os.system('calc') # 运行系统的shell命令  打开计算器
print(os.sep) # 输出操作系统的路径分隔符，linux为/,windows为\\

print(os.getcwd())
print(os.path.abspath(os.getcwd()))
print(os.path.abspath(os.path.dirname(os.getcwd())))  # 返回当前文件夹的上层目录
print(os.path.abspath(os.path.dirname(os.path.dirname(os.getcwd())))) # 返回当前文件夹的上上层目录

'''os.path模块关于路径常用方法'''
print(os.path.basename('E:\\A\\B\\C\\a.ini')) # a.ini
print(os.path.dirname('E:\\A\\B\\C\\a.ini'))  # E:\A\B\C
print(os.path.join('E:\\','11','A','B'))
print(os.path.split('E:\\A\\B\\C\\a.ini'))
print(os.path.split('E:\\A\\B\\C'))
print(os.path.splitext('E:\\A\\B\\C\\a.ini'))

# os.path.isdir()
# os.path.isfile()
# os.path.isabs() # 是否绝对路径
# os.path.exists() # 指定目录文件是否存在

dirs=r'C:\22code\RF'
if  os.path.exists(dirs):
    files=os.listdir(dirs,)
    os.path.join(dirs,files[0])
    os.path.isfile()
    os.path.isdir()

os.listdir()
os.mkdir()
os.rmdir()
os.makedirs()
os.removedirs()
os.chdir()
os.rename()

os.getcwd()

# os.system(r'C:\"Program Files"\"Internet Explorer"\iexplore.exe') #文件路径包括空格，此方法不能直接处理，所以用了""，用下面的方法更好
# os.startfile(r'C:\Program Files\Internet Explorer\iexplore.exe')

import os

path='F:\luan'
# print help(os.walk)
for root,d,filelist in os.walk(path):
    for file in filelist:
        print(os.path.join(root,file))


def blpath(path):
    listdir=os.listdir(path)
    for dirname in listdir:
        pathname=os.path.join(path,dirname)
        if os.path.isdir(pathname):
            blpath(pathname)
        else:
            print(pathname)


path='F:\luan'
blpath(path)