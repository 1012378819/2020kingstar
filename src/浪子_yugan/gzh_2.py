# -*- coding: utf-8 -*-
"""
@time: 2020/2/9 13:18
@author: pei.lu
"""
# http.sever模块实现web应用
from http.server import ThreadingHTTPServer,BaseHTTPRequestHandler
from urllib.parse import urlparse,parse_qs

class PageHandle(BaseHTTPRequestHandler):
    """响应客户端请求"""

    def get_argument(self,key,default=None):
        """从QueryString参数或form参数中返回指定的参数"""

        query_dict=parse_qs(urlparse(self.path).query) # 解析QueryString参数
        try:
            form_dict=parse_qs(self.rfile.read(int(self.headers['content-length'])))
        except:
            form_dict=None

        if form_dict and key.encode('utf8') in form_dict:
            return form_dict[key.encode('utf8')][0].decode('utf8')

        if key in query_dict:
            return query_dict[key][0]

        return default

    def do_GET(self):
        """响应GET请求"""

        answer=self.get_argument('answer','') # 获取上次结果
        html="""
            <!DOCTYPE html>
            <html>
              <head>
                <title>在线计算器</title>
                <meta charset="utf-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
              </head>
              <body>
                <h3 style="color:#ff0000;">请输入算式：</h3>
                <form action="/" method="POST">
                  <input type="text" name="expression" value="%s"/>
                  <button type="submit">确定</button>
                </form>
              </body>
            </html>
        """%answer

        self.send_response(200)
        self.send_header('Content_type','text/html;charset=UTF-8')
        self.end_headers()
        self.wfile.write(html.encode('utf8'))

    def do_POST(self):
        """响应POST请求"""
        expression=self.get_argument('expression') # 获取form提交的expression参数
        print(expression)
        if expression:
            try:
                answer=eval(expression)
            except:
                answer='Error'

        self.send_response(302)
        self.send_header('Location','\?answer=%s'%answer)
        self.end_headers()

if __name__ == '__main__':
    server=ThreadingHTTPServer(('',8080),PageHandle)
    server.serve_forever()