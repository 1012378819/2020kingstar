# -*- coding: utf-8 -*-
"""
@time: 2020/2/27 8:44
@author: pei.lu
"""
# 1、python如何管理项目：版本控制，虚拟环境
#
# 2、py2和py3的区别
#
# 3、编程题：求一个串中第二大数，不止一个时并输出个数，要求一次遍历
#
# 4、编程题：爬台阶，每次你可以爬1 或2 个台阶。你有多少种不同的方法可以爬到楼顶呢？
#
# 5、编程题：n*m的矩阵，从左上角出发，每次走一步，只能向前和向下走，到达右下角有多少种走法？
#
# 6、编程题：一个数组B先降序在升序，查找目标s
#
# 7、编程题：两个有序数组合并成一个有序数组
#
# 8、编程题：一个文件很大，且里面都是ip地址，让你找出出现频率最高的10个IP。
#
# 9、深copy和浅copy的区别
#
# 10、元组和链表的区别
#
# 11、Redis的了解，常见的操作

# 4、编程题：爬台阶，每次你可以爬1 或2 个台阶。你有多少种不同的方法可以爬到楼顶呢？
#
# n级台阶
# (1,2,1,2...1)
# n/2 n个数，随机生成[n/2 ,n]个数在（0,1）中 ，序列和=n (n>=1)
# n=1 , (1)              1
# n=2,  (1,1) (2)        2
# n=3,(1,2)(2,1)(1,1,1)  3
# n=4,(1,1,1,1)(2,1,1)(1,1,2)(1,2,1)(2,2)  5
# n=5,  0 个2 ，1个2， 2个2   （1+4+3）= 8



