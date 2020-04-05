import mysql.connector
# import MySQLdb
# import pymysql

# 上下文管理协议：包含方法 __enter__()和__exit__()，支持该协议的对象要实现这两个方法
class UseDatabase:
    def __init__(self,config:dict) ->None :
        self.configuration=config
        
    def __enter__(self) ->'cursor':
        self.conn=mysql.connector.connect(**self.configuration)
        # self.conn=MySQLdb.connect(**self.configuration)
        self.cursor=self.conn.cursor()
        return self.cursor
    
    def __exit__(self, exc_type, exc_val, exc_trace) ->None:
        self.conn.commit()
        self.cursor.close()
        self.conn.close()


