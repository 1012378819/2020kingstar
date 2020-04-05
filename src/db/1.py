# -*- coding: utf-8 -*-
'''
Created on 2019年3月25日

@author: weiwei.sun
'''
# import cx_Oracle
import sys
#from public.log import log
import mysql.connector
import pymysql

class whileXh():

    def __init__(self, dbuser=None, dbpwd=None, dbhost=None):
        self.dbuser = dbuser
        self.dbpwd = dbpwd
        self.dbhost = dbhost
        self.conn = False

    def connectOracle(self):
        try:
            databaseName = self.dbuser + '/' + self.dbpwd + '@' + self.dbhost
            self.conn = cx_Oracle.connect(databaseName)
            self.cursor = self.conn.cursor()
        except:
            print('fail:connect database failed')
            self.conn = False
        return self.conn

    def whileXh(self, sql):

        result = False
        if (self.conn):

            try:
                self.cursor.execute(sql)
                '''取所有结果的值
                reslut = self.cursor.fetchall()   '''
                result = self.cursor.fetchone()
                istatus = result[0][0]
                while (istatus != '1' and istatus != "2"):
                    self.cursor.execute(sql)
                    result = self.cursor.fetchone()
                    istatus = result[0][0]
                result = True
            except:
                result = False
                print('fail:query database is fail:%s' % sql)
        else:
            print('fail:fect_all:database is not connect')
        return result

# test = whileXh("ivsd", "ivsd", '10.253.147.11')
# test.connectOracle()
# sql = 'select * from custominfo'
# test.whileXh(sql)
