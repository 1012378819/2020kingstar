# -*- coding: utf-8 -*-
"""
@time: 2020/2/9 21:06
@author: pei.lu
"""
# 安装方式 pip install PyMySQL
# 以元组形式返回查询记录
# 如果把代码中的 pymysql 改为 MySQLdb，可以轻松切换成 mysqlclient 模块。
import pymysql
db=pymysql.connect(
    host='localhost',
    user='xufive',
    password='******',
    db='demo',
    charset='utf8'
)
cursor=db.cursor()
cursor.execute('select * from member where id=%s',(100,))
print(cursor.fetchall()) # 以元组形式返回查询记录
# ((100, '370103********0012', '*9EE8E3304D69C3E9260F19C224EA5852129BF030', '王茁洋', '男', datetime.date(****, **, **), '', '济南', '济南泉景小学', '186********', Decimal('1812.50')),)
cursor.close()
db.close()

# 事务回滚

def transaction(db):
    try:
        db.begin()
        # 此处加入出错之后需要回滚的数据库操作
        db.commit()
        return True
    except:
        db.rollback()
        return False




