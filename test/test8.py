#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'igis_gzy'

from routes import Mapper

map = Mapper()  #生成的是 Mapper()实例对象
print map
print type(map)

map.connect('lixin', '/blog', controller = 'main', action = 'index')

result = map.match('/blog')
print result

