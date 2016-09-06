__author__ = 'igis_gzy'  # P349
#!usr/bin/python

from BaseHTTPServer import HTTPServer
from SimpleHTTPServer import SimpleHTTPRequestHandler

serveraddr = ('', 8765)
srvr = HTTPServer(serveraddr, SimpleHTTPRequestHandler)
srvr.serve_forever()


