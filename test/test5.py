#!/usr/bin/env python
# -*- coding: utf-8 -*-
# https://my.oschina.net/crooner/blog/609030
__author__ = 'igis_gzy'

from wsgiref.simple_server import make_server
from webob import Request, Response
from webob.dec import *
from routes import Mapper, middleware

class images(object):
    def index(self):
        return "images do index()"
    def create(self):
        return "images do create()"
    def detail(self):
        return "images do detail()"

class servers(object):
    def index(self):
        return "servers do index()"
    def create(self):
        return "servers do create()"
    def detail(self):
        return "servers do detail()"

class APIRouter(object):
    def __init__(self):
        print '__init__'
        self.controller = None
        m = Mapper()
        m.connect('blog', '/{class_name}/{action}/{id}',
                  conditions={'method': ['GET']})
        m.redirect('/', '/servers/index/1')
        self.router = middleware.RoutesMiddleware(self.dispatch, m)
        print self.router

    @wsgify
    def dispatch(self, req):
        match = req.environ['wsgiorg.routing_args'][1]
        print req.environ['wsgiorg.routing_args']
        if not match:
            return 'error url: %s' % req.environ['PATH_INFO']

        class_name = match['class_name']
        self.controller = globals()[class_name]()

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
    httpd = make_server('0.0.0.0', 8000, APIRouter())
    print "Listening on port 8000...."
    httpd.serve_forever()
