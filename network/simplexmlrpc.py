#!usr/bin/python  P356
from SimpleXMLRPCServer import SimpleXMLRPCServer, SimpleXMLRPCRequestHandler
from SocketServer import ThreadingMixIn

class Math:
    def pow(self, x, y):
        """Return x raised to the yth power; that is, x ** y.
        x and y may be integers or floating-point values."""
        return x ** y

    def hex(self, x):
        """Return a string holding a hexadecimal representation of the integer x. """
        return "%x" % x

class ThreadingServer(ThreadingMixIn, SimpleXMLRPCServer):
    pass

serveraddr = ('', 8765)
srvr = ThreadingServer(serveraddr, SimpleXMLRPCRequestHandler)
srvr.register_instance(Math())
srvr.register_introspection_functions()
srvr.serve_forever()


