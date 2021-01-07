# -*- coding:utf-8 -*-
from http.server import BaseHTTPRequestHandler, HTTPServer
import os


class RequestHandler(BaseHTTPRequestHandler):
    # 处理请求并返回页面

    # 页面模板
    Page = '''\
        <html>
        <body>
        <p>Hello, web!</p>
        </body>
        </html>
    '''

    # 处理一个GET请求
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-Type", "text/html")
        self.send_header("Content-Length", str(len(self.Page)))
        self.end_headers()
        self.wfile.write(self.Page.encode('utf-8'))
        xb = os.path.join(os.path.expanduser('~'), 'Desktop')
        with open(xb + '/test2.txt', mode='w', encoding='utf-8') as f:
            f.write("当前登录用户是：" + os.getlogin())
            f.close()
            print("看你的桌面")


if __name__ == '__main__':
    serverAddress = ('127.0.0.1', 8090)
    server = HTTPServer(serverAddress, RequestHandler)
    server.serve_forever()
