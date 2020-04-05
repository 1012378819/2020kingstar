# -*- coding: utf-8 -*-
"""
@time: 2020/2/9 21:13
@author: pei.lu
"""
# 安装方式 pip install mysqlclient
# 以字典形式返回查询记录
# 如果把代码中的 MySQLdb 改为 pymysql，可以轻松切换成 PyMySQL 模块。
import MySQLdb.cursors
db=MySQLdb.connect(
    host='localhost',
    user='xufive',
    password='******',
    db='demo',
    charset='utf8',
    cursorclass=MySQLdb.cursors.DictCursor
)
with db.cursor() as cursor :
    sql='select * from member where id=%s'
    cursor.execute(sql,(100,))
    print(cursor.fetchall()) # 以字典形式返回
    # ({'id': 100, 'idcard': '370103********0012', 'passwd': '*9EE8E3304D69C3E9260F19C224EA5852129BF030', 'name': '王茁洋', 'sex': '男', 'birthday': datetime.date(****, **, **), 'title': '', 'address': '济南', 'club': '济南泉景小学', 'phone': '186********', 'rating': Decimal('1812.50')},)
