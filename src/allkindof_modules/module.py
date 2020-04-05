import webbrowser
webbrowser.open('http://www.baidu.com')

import copy
# print(copy.__all__) #定义了模块的公共接口，在from copy import * 时就默认只能使用这些函数
# print (help(copy.copy))
# print(copy.__doc__) #查看文档描述字符串
# print(copy.__file__) #查找源代码位置

# import sys
# print(sys.__doc__)
# args=sys.argv[1:] #命令行参数，放在sys.argv列表中,第一个元素是脚本的名字
# args.reverse() #返回None的原地修改操作
# print(''.join(args))  #shell中执行 $python module.py this is a test,那结果返回test a is this

# >>> import sys
# >>> sys.path
# ['', '/Library/Frameworks/Python.framework/Versions/3.6/lib/python36.zip', '/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6', ..., '/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/site-packages']
# 如果我们要添加自己的搜索目录，有两种方法：
#
# 一是直接修改sys.path，添加要搜索的目录：
# >>> import sys
# >>> sys.path.append('/Users/michael/my_py_scripts')
# 这种方法是在运行时修改，运行结束后失效。
# 
# 第二种方法是设置环境变量PYTHONPATH，该环境变量的内容会被自动添加到模块搜索路径中。设置方式与设置Path环境变量类似。
# 注意只需要添加你自己的搜索路径，Python自己本身的搜索路径不受影响。

# 以下情况是告诉编译器去哪儿找的原因：
# 　　** 不希望将自己的模块填满python解释器的目录
# 　　** 没有在python解释器目录中存储文件的权限
# 　　** 想将模块放到其它位置

