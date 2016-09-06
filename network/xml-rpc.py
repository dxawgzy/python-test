#!usr/bin/python  #P160

import xmlrpclib
url = 'http://www.w3school.com.cn/jsref/prop_node_nodetype.asp'
s = xmlrpclib.ServerProxy(url)
catdata = s.meerkat.getCategrories()
cattitles = [item['title'] for item in catdata]
cattitles.sort()
for item in cattitles:
    print item



