#!/usr/bin/env python
# -*- coding: utf-8 -*-
# https://my.oschina.net/crooner/blog/609030
__author__ = 'igis_gzy'

from wsgiref.simple_server import make_server
from webob import Request, Response

#application
class AppTestByManual(object):
    def __call__(self, environ, start_response):
        req = Request(environ)
        return self.test(environ, start_response)

    def test(self, environ, start_response):
        res = Response()
        res.status = 200     #middleware
        res.body   = "spch"  #middleware
        return res(environ, start_response)

application = AppTestByManual()

#server
httpd = make_server('0.0.0.0', 8000, application)
httpd.serve_forever()
