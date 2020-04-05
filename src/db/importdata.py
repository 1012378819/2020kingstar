import sqlite3
def convert(value):
    if value.startswith('~'):
        return value.strip('~')
    if not value:
        value='0'
    return float(value)

conn=sqlite3.connect('food.db')
curs=conn.cursor()

curs.execute("""
CREATE TABLE food(
 id    TEXT   primary key ,
 desc  TEXT,
 water  FLOAT,
 kcal   FLOAT,
 fat    FLOAT,
 sugar  FLOAT
)
""")

query="INSERT INTO food VALUES (?,?,?,?,?,?)"

for line in open('ab.txt'): #文件内容示例~08453~^~HORMEL SPAM... W...~^...
    fields=line.split('^')
    vals=[convert(f) for f in fields[:fields.count]]
    curs.execute(query,vals)

conn.commit()
conn.close()

