# -*- coding: utf-8 -*-
"""
@time: 2020/3/15 20:01
@author: pei.lu
"""
import logging
# 日志共分5个等级，从低到高见下面5种，默认收集warning以上等级的日志
# logging.debug('这是debug等级日志信息')
# logging.info('这是info等级日志信息')
# logging.warning('这是warning等级日志信息')
# logging.error('这是error等级日志信息')
# logging.critical('这是critical等级日志信息')

my_log=logging.getLogger('my_log') # 创建自己的日志收集器
my_log.setLevel('DEBUG')

l_s=logging.StreamHandler() # 日志输出到控制台
l_s.setLevel("INFO")
l_f=logging.FileHandler('log.log',encoding='utf8') # 日志输出到文件中
l_f.setLevel("DEBUG")
my_log.addHandler(l_s)
my_log.addHandler(l_f)

# 设置日志格式
ft="%(asctime)s - [%(filename)s --> line:%(lineno)d] - %(levelname)s: %(message)s"
ft=logging.Formatter(ft)
l_s.setFormatter(ft)
l_f.setFormatter(ft)
# 日志输出
my_log.debug("--my_log_debug--")
my_log.info("--my_log_info--")
my_log.warning("--my_log_warning--")
my_log.error("--my_log_error")
my_log.critical("--my_log_critical")