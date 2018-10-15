#!/usr/bin/env python
# -*- coding: utf-8 -*-
# https://my.oschina.net/crooner/blog/609030
__author__ = 'igis_gzy'

from wsgiref.simple_server import make_server
from webob import Request, Response
from webob.dec import *
from routes import Mapper, middleware

class Test(object):
    def index(self):
        return "do index()"
    def add(self):
        return "do show()"

class MyApp(object):
    def __init__(self):
        print '__init__'
        self.controller = Test()
        m = Mapper()
        m.connect('blog', '/blog/{action}/{id}', controller=Test,
                  conditions={'method': ['GET']})
        m.redirect('/', '/blog/index/1')
        self.router = middleware.RoutesMiddleware(self.dispatch, m)

    @wsgify
    def dispatch(self, req):
        match = req.environ['wsgiorg.routing_args'][1]
        print req.environ['wsgiorg.routing_args']
        if not match:
            return 'error url: %s' % req.environ['PATH_INFO']
        action = match['action']
        if hasattr(self.controller, action):
            func = getattr(self.controller, action)
            ret = func()
            return ret
        else:
            return "has no action:%s" % action

    @wsgify
    def __call__(self, req):
        print '__call__'
        return self.router

if __name__ == '__main__':
    httpd = make_server('0.0.0.0', 8000, MyApp())
    print "Listening on port 8000...."
    httpd.serve_forever()
