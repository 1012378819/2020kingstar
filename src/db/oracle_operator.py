import cx_Oracle

con = cx_Oracle.connect('v8user/v8user@10.253.46.100:1521/futures8')   #FUTURE8_117
cursor = con.cursor()

cursor.execute('select * from tt_cust_info')
rows = cursor.fetchall()
names = cursor.description
a = len(rows)
print(a)
for row in rows:
    print('%s,%s,%s' %(row[0],row[1],row[2]))
print('Number of rows returned:%d' % cursor.rowcount)
for name in names:
    print(name[0])

cursor.execute('select * from TR_CUST_RISK_NOTIFY_INFO  order by notify_date,jour_no')
while(True):
    row = cursor.fetchone()
    if row == None:
        break
    print(row)

cursor.close()
con.close()

