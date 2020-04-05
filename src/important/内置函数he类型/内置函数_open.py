# -*- coding: utf-8 -*-
"""
@time: 2020/2/27 13:37
@author: pei.lu
"""
# open函数是python的一个内置函数，用于打开一个文件，创建一个 file 对象。
# open(name[, mode[, buffering]])
# file 对象方法
# file.read([size])：size 未指定则返回整个文件，如果文件大小 >2 倍内存则有问题，f.read()读到文件尾时返回""(空字串)。
# file.readline()：返回一行。
# file.readlines([size]) ：返回包含size行的列表, size 未指定则返回全部行。
# for line in f: print line ：通过迭代器访问。
# f.write("hello\n")：如果要写入字符串以外的数据,先将他转换为字符串。
# f.tell()：返回一个整数,表示当前文件指针的位置(就是到文件头的比特数)。
# f.seek(偏移量,[起始位置])：用来移动文件指针。
# ·偏移量: 单位为比特，可正可负
# ·起始位置: 0 - 文件头, 默认值; 1 - 当前位置; 2 - 文件尾
# f.close() 关闭文件