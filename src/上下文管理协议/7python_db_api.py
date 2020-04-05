import mysql.connector

def log_request(req:'flask_request',res:str) ->None :
    """log details of the web request and the result."""
    dbconfig={
        'host':'127.0.0.1',
        'user':'vsearch',
        'password':'vsearchpwd',
        'database':'vsearchDB'
    }
    conn=mysql.connector.connect(**dbconfig)
    cursor=conn.cursor()
    _SQL="""insert into catalog
            (phrase,letters,ip,browser_string,results)
            values
            (%s,%s,%s,%s,%s)"""
    cursor.execute(_SQL,(req.form['phrase'],
                         req.form['letters'],
                         req.remote_addr,
                         req.user_agent.browser,
                         res,))
    conn.commit()
    cursor.close()   #游标会返回一个True来确认已经成功关闭，而连接只是直接关闭
    conn.close()