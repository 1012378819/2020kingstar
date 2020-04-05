# -*- coding: utf-8 -*-
"""
@time: 2020/2/11 15:25
@author: pei.lu
"""
import os
import sqlite3

class WaterDB:
    """水位数据库"""
    def __init__(self):
        """构造函数"""
        fn_db='spring.db'
        is_db=os.path.exists(fn_db)

        self._conn=sqlite3.connect(fn_db)
        self._cur=self._conn.cursor()
        if not is_db:
            self._create_table()

    def _create_table(self):
        """创建表spring，共三个字段"""
        sql='''CREATE TABLE spring(
        id INTEGER PRIMARY KEY AUTHORIZATION ,
        date DATE,
        bt REAL,
        hh READ 
        )'''
        self._execute(sql)
        self._conn.commit()

    def _execute(self,sql,args=()):
        """运行sql语句"""
        if isinstance(args,list): # 批量执行SQL语句，此时parameter是list，其元素是tuple
                                  # 例如[('2010-10-10', 28.22, 28.17, '2017-10-10'),('2012-01-31', 28.57, 28.51, '2013-01-31'),]
            self._cur.executemany(sql,args)
        else: # 单次执行SQL语句，此时parameter是tuple或者None
            self._cur.execute(sql,args)

        if sql.split()[0].upper()!='SELECT': # 非select语句，则执行commit()
            self._conn.commit()

        return self._cur.fetchall()

    def close(self):
        """关闭数据库连接"""
        self._cur.close()
        self._conn.close()
        
    def append(self,data):
        sql='INSERT INTO spring (data,bt,hh) values (?,?,?)'
        self._execute(sql,data)

    def rectify(self, err_list):
        """更新已知的日期错误"""

        for item in err_list:
            if item[3]:
                sql = 'update spring set date=? where date=? and bt=? and hh=?'
                self._execute(sql, (item[3], item[0], item[1], item[2]))
            else:
                sql = 'delete from spring where date=? and bt=? and hh=?'
                self._execute(sql, (item[0], item[1], item[2]))
if __name__ == '__main__':
    pass
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
