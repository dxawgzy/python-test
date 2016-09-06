#coding=utf8
#!usr/bin/python  #P350

from SocketServer import ThreadingMixIn, TCPServer, StreamRequestHandler
import time

class TimeRequestHandler(StreamRequestHandler):
    def handle(self):
        req = self.rfile.readline().strip()
        if req == "asctime":
            result = time.asctime()
        elif req == "seconds":
            result = str(int(time.time()))
        elif req == "rfc822":
            result = time.strftime("%a, %d %b %Y %H:%M:%S +0000", time.gmtime())
        else:
            result = """Unhandled request. Send a line with one of the following words:
                asctime -- for human-readable time
                seconds -- seconds since the Unix Epoch
                rfc822 -- date/time in format used for mail and news posts
                """
        self.wfile.write(result + "\n")

class TimeServer(ThreadingMixIn, TCPServer):
    allow_reuse_address =1

serveraddr = ('', 8765)
srvr = TimeServer(serveraddr, TimeRequestHandler)
srvr.serve_forever()

"""
此程序的功能不能再浏览器予以验证，通过 telnet localhost 8765 连接成功后
分别输入 asctime  seconds rfc822 可以分别显示对应格式的时间
输入其他内容时，会输出程序中写的提示信息

asctime
Fri Apr 29 16:43:45 2016

seconds
1461919521

rfc822
Fri, 29 Apr 2016 08:42:39 +0000

"""


