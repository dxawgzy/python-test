#coding=utf-8
#! usr/bin/python  #P115 6.1 python网络编程
import sys, urllib2

req = urllib2.Request(sys.argv[1])
fd = urllib2.urlopen(req)
print "Retrieved", fd.geturl()
info = fd.info()
#print info
for key, value in info.items():
    print "%s = %s" %(key, value)

#python dump_info.py http://httpd.apache.org/dev
"""
Retrieved http://httpd.apache.org/dev/
content-length = 8407
accept-ranges = bytes
vary = Accept-Encoding
server = Apache/2.4.7 (Ubuntu)
last-modified = Sat, 20 Feb 2016 10:44:41 GMT
connection = close
etag = "20d7-52c3149824b03"
date = Wed, 13 Apr 2016 08:31:16 GMT
content-type = text/html
"""

