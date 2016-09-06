#coding=utf-8  #中文注释必须加上这句，否则报错
#!usr/bin/python  #P226 Twisted 使用回调函数callback function

from twisted.internet import defer, reactor, protocol
#from twisted.protocols.imap4 import IMAP4Client
from twisted.mail.imap4 import IMAP4Client
import sys

class IMAPClient(IMAP4Client):
    def connectionMade(self):
        print "I have successfully connected to the server!"
        d = self.getCapabilities()
        d.addCallback(self.gotcapabilities)
        #在addCallback()中，对gotcapabilities的调用未使用括号()，即gotcapabilities()
        #因为不想在调用addCallback()的时候调用gotcapabilities()，
        #只是把函数传递给addCallback()，并让Twisted稍后调用它。

    def gotcapabilities(self, caps):
        if caps == None:
            print "Server did not return a capability list."
        else:
            for key, value in caps.items():
                print "%s: %s" % (key, str(value))

        self.logout()
        reactor.stop()
        #直到reactor.stop()被调用，对reactor.run()的调用才返回。

class IMAPFactory(protocol.ClientFactory):
    protocol = IMAPClient

    def clientConnectionFailed(self, connector, reason):
        print "Client connection failed:", reason
        reactor.stop()

reactor.connectTCP(sys.argv[1], 143, IMAPFactory())
reactor.run()



