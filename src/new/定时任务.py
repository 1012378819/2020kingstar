# -*- coding:utf-8 -*-
# @Time : 2020/4/6 15:49
# @Author: lup
__author__ = 'pei.lu'

import schedule,time

def job():
    print('hi')

schedule.every(1).minutes.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)