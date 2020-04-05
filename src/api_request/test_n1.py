#coding:utf-8
import requests
data={
    'type':'zjsq',
    'ApplyId':'aabbcc',
    'IsApprove':'yes'
}
#r=requests.get('http://127.0.0.1:80')
req=requests.post('http://127.0.0.1',json=data)
# print(r.status_code)
# print(r)
print(req.status_code)
print(req.text)
print(req.content)


# r1=requests.get('http://127.0.0.1:8010/cgi-bin/greeting.py?zjsqid=11&ISApprove=approve')
# r2=requests.post('http://127.0.0.1:8010/cgi-bin/greeting.py',data=data)

# r1=requests.get('http://127.0.0.1:8011/cgi_test.py?zjsqid=11&ISApprove=approve')
# r2=requests.post('http://127.0.0.1:8011/cgi_test.py',data=data)
#
# print(r1.status_code)
# print(r1.content)
# print(r1.text)
# print(r2.status_code)
# print(r2.content)
# print(r2.text)

