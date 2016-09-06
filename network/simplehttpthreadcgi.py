#coding=utf8
#!usr/bin/python  #P349和P350两个程序二合一
from BaseHTTPServer import HTTPServer
#from SimpleHTTPServer import SimpleHTTPRequestHandler
from CGIHTTPServer import CGIHTTPRequestHandler
from SocketServer import ThreadingMixIn

class ThreadingServer(ThreadingMixIn, HTTPServer):
    pass

serveraddr = ('', 8765)
#srvr = ThreadingServer(serveraddr, SimpleHTTPRequestHandler)
srvr = ThreadingServer(serveraddr, CGIHTTPRequestHandler)
srvr.serve_forever()

#CGI程序运行方式：假设CGI程序为 myscript.cgi，通过浏览器访问 http://localhost:8765/myscript.cgi



