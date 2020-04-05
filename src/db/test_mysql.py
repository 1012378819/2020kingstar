# coding=utf-8
import time
import MySQLdb

try:
    conn = MySQLdb.connect(host='127.0.0.1', user='root', passwd='', db='dpms', port=3306)
    cur = conn.cursor()
    cur.execute('insert into test values(0,"x0")')
    conn.commit()
    cur.close()
    conn.close()
    print("finish insert direct")
except MySQLdb.Error as e:
    print(e.args[1])

try:
    conn = MySQLdb.connect(host='127.0.0.1', user='root', passwd='', db='dpms', port=3306)
    cur = conn.cursor()
    cur.execute('insert into test values(%s,%s)', (1, "x1"))
    cur.execute('insert into test values(%s,%s)', [2, "x2"])
    conn.commit()
    cur.close()
    conn.close()
    print("finish insert by para")
except MySQLdb.Error as e:
    print(e.args[1])

try:
    conn = MySQLdb.connect(host='127.0.0.1', user='root', passwd='', db='dpms', port=3306)
    cur = conn.cursor()
    data = []
    data.append((3, "x3"))
    data.append((4, "x4"))
    cur.executemany('insert into test values(%s,%s)', data)
    data = []
    data.append([5, "x5"])
    data.append([6, "x6"])
    cur.executemany('insert into test values(%s,%s)', data)
    conn.commit()
    cur.close()
    conn.close()
    print("finish muti insert by para")
except MySQLdb.Error as e:
    print(e.args[1])

try:
    conn = MySQLdb.connect(host='127.0.0.1', user='root', passwd='', db='dpms', port=3306)
    cur = conn.cursor()
    cur.execute('select * from test where id=%s', ('2'))  # 数字参数?
    res = cur.fetchall()
    for re in res:
        print("id=%s,info=%s" % (re[0], re[1]))
    cur.close()
    conn.close()
    print("finish query where")
except MySQLdb.Error as e:
    print(e.args[1])

try:
    conn = MySQLdb.connect(host='127.0.0.1', user='root', passwd='', db='dpms', port=3306)
    cur = conn.cursor()
    cur.execute('select * from test')
    res = cur.fetchall()
    for re in res:
        print("id=%s,info=%s" % (re[0], re[1]))
    cur.close()
    conn.close()
    print("finish query fetchall")
except MySQLdb.Error as e:
    print(e.args[1])

try:
    conn = MySQLdb.connect(host='127.0.0.1', user='root', passwd='', db='dpms', port=3306)
    cur = conn.cursor()
    cur.execute('select * from test')  # 游标指向第一条记录
    re = cur.fetchone()  # 获取当前游标记录，同时游标指向下一条记录
    print("id=%s,info=%s" % (re[0], re[1]))
    re = cur.fetchone()
    print("id=%s,info=%s" % (re[0], re[1]))
    res = cur.fetchall()  # 获取当前游标记录及后续所有记录
    for re in res:
        print("id=%s,info=%s" % (re[0], re[1]))
    cur.close()
    conn.close()
    print("finish query fetchone")
except MySQLdb.Error as e:
    print(e.args[1])

try:
    conn = MySQLdb.connect(host='127.0.0.1', user='root', passwd='', db='dpms', port=3306)
    cur = conn.cursor()
    cur.execute('delete from test')
    conn.commit()
    cur.close()
    conn.close()
    print("finish delete")
except MySQLdb.Error as e:
    print(e.args[1])

# 需要说明的是，如果python脚本的字符集编码与数据库的字符集不一致，中文会出现乱码。
#
# 解决方法是在获取链接时指定数据库的字符集。如：
#
# conn = MySQLdb.connect(host='127.0.0.1', user='root', passwd='', db='dpms', port=3306, charset='gbk')
