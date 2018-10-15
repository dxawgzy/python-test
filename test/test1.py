#!usr/bin/python
#coding=utf-8
# http://www.liaoxuefeng.com/wiki/001374738125095c955c1e6d8bb493182103fac9270762a000/001386832689740b04430a98f614b6da89da2157ea3efe2000
__author__ = 'igis_gzy'

from wsgiref.simple_server import make_server

# def application(environ, start_response):
#     start_response('200 OK', [('Content-Type', 'text/html')])
#     return '<h1>Hello, web!</h1>'

def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    return '<h1>Hello, %s!</h1>' % (environ['PATH_INFO'][1:] or 'web')

# 创建一个服务器，IP地址为空，端口是8000，处理函数是application:
httpd = make_server('', 8000, application)
print "Serving HTTP on port 8000..."
# 开始监听HTTP请求:
httpd.serve_forever()
