#coding=utf8
#!usr/bin/python  #P160  XML-RPC自省

import xmlrpclib, sys

#url = 'http://www.oreillynet.com/meerkat/xml-rpc/server.php'
url = 'http://localhost:8765/'
s = xmlrpclib.ServerProxy(url)

print "Gathering available methods..."
methods = s.system.listMethods()
while 1:
    print "\n\nAvailable Methods:"
    for i in range(len(methods)):
        print "%2d: %2s" % (i + 1, methods[i])
    selection = raw_input("Select one number (q to quit):")
    if selection == 'q':
        break
    item = int(selection) - 1
    print "\n**********"
    print "Details for %s\n" % methods[item]

    for sig in s.system.methodSignature(methods[item]):
        print "Args: %s; Returns: %s" % (", ".join(sig[1:]), sig[0])
    print "Help:", s.system.methodHelp(methods[item])

#最后三行代码应该在while循环之内，书中（P161）写到了while之外，有误
#本程序结合simplexmlrpc.py（P356）使用时，将url改为 localhost:8765



