#coding=utf8
#!usr/bin/python  #342

from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler

class RequestHandler(BaseHTTPRequestHandler):
    def _writeheaders(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_HEAD(self):
        self._writeheaders()

    def do_GET(self):
        self._writeheaders()
        self.wfile.write("""<HTML><HEAD><TITLE>Sample Page</TITLE></HEAD>
            <BODY>This is a sample HTML page. Every page this server provides
            will look like this.</BODY></HTML>""")

serveraddr = ('', 8765)
srvr = HTTPServer(serveraddr, RequestHandler)
srvr.serve_forever()


"""
在命令行运行 telnet localhost 8765 后在弹出的新页面中输入  HEAD / HTTP/1.0
(在命令行中输入时，实际看不到这句话)，连续敲击两次回车机会有返回结果

HTTP/1.0 200 OK
Server: BaseHTTP/0.3 Python/2.7.10
Date: Wed, 27 Apr 2016 06:16:16 GMT
Content-type: text/html

遗失对主机的连接。


telnet localhost 8765 后在弹出的新页面中输入  GET / HTTP/1.0  连续敲击两次回车

HTTP/1.0 200 OK
Server: BaseHTTP/0.3 Python/2.7.10
Date: Wed, 27 Apr 2016 06:08:56 GMT
Content-type: text/html

<HTML><HEAD><TITLE>Sample Page</TITLE></HEAD>
        <BODY>This is a sample HTML page. Every page this server provides
        will look like this.</BODY></HTML>

遗失对主机的连接。


直接在浏览器输入 http://localhost:8765  也可看到结果
"""

