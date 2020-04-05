# -*- coding: utf-8 -*-
"""
@time: 2020/2/24 13:27
@author: pei.lu
"""
import pymysql

class MysqlDB(object):
  '''连接mysql'''

  def __init__(self, config):
    self.conn = pymysql.connect(**config)
    self.cursor = self.conn.cursor()

  def execute(self, sql, data=None, is_commit=True):
    '''单行插入'''
    self.conn.ping(reconnect=True)  # 在进行操作前ping下连接，检查连接是否断开，如果断开（断开会引发错误）连接就进行一次重连，该接口封装了以上逻辑
    self.cursor.execute(sql, data)
    if is_commit:
      self.conn.commit()

  def executemany(self, sql, data, is_commit=True):
    '''多行插入'''
    self.conn.ping(reconnect=True)
    self.cursor.executemany(sql, data)
    if is_commit:
      self.conn.commit()

  def queryone(self, sql, data=None):
    self.conn.ping(reconnect=True)
    self.cursor.execute(sql, data)
    return self.cursor.fetchone()

  def queryall(self, sql, data=None):
    self.conn.ping(reconnect=True)
    self.cursor.execute(sql, data)
    return self.cursor.fetchall()

  def getrowid(self, sql, data=None):
    self.conn.ping(reconnect=True)
    self.cursor.execute(sql, data)
    return self.cursor.lastrowid

  def rollback(self):
    self.conn.ping(reconnect=True)
    self.conn.rollback()

  def commit(self):
    self.conn.ping(reconnect=True)
    self.conn.commit()

  def __del__(self):
    self.cursor.close()
    self.conn.close()