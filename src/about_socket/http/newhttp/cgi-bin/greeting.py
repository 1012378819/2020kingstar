import cgi
form=cgi.FieldStorage()
print('Content-type:text/html\n')
name=form['zjsqid'].value +form['ISApprove'].value
print('<h1>hello %s </h1>'%name)

#get请求
#http://127.0.0.1:8010/cgi-bin/greeting.py?zjsqid=11&ISApprove=approve

#post请求
#http://127.0.0.1:8010/greeting.html

