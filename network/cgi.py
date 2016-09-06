__author__ = 'igis_gzy'
#!usr/bin/python   #P366
from SimpleXMLRPCServer import CGIXMLRPCRequestHandler
import time

class Stats:
    def getstats(self):
        return self.callstats

    def getruntime(self):
        return time.time() - self.starttime

    def failure(self):
        raise RuntimeError, "This function always raises an error."

class Math(Stats):
    def __init__(self):
        self.callstats = {'pow': 0, 'hex': 0}
        self.starttime = time.time()

    def pow(self, x, y):
        return pow(x, y)

    def hex(self, x):
        self.callstats['hex'] += 1
        return "%x" % x

handler = CGIXMLRPCRequestHandler()
handler.register_instance(Math())
handler.register_introspection_functions()
handler.handle_request()



