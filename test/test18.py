#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'igis_gzy'

# def decorator_a(func):
#     print 'Get in decorator_a'
#     def inner_a(*args, **kwargs):
#         print 'Get in inner_a'
#         return func(*args, **kwargs)
#     return inner_a
#
# def decorator_b(func):
#     print 'Get in decorator_b'
#     def inner_b(*args, **kwargs):
#         print 'Get in inner_b'
#         return func(*args, **kwargs)
#     return inner_b
#
# @decorator_b
# @decorator_a
# def f(x):
#     print 'Get in f'
#     return x * 2
#
# f(1)

'''
igis_gzy@CT-032515265640 MINGW64 /e/python/python-test/test (master)
$ python test18.py
Get in decorator_a
Get in decorator_b
Get in inner_b
Get in inner_a
Get in f
'''


def decorator_a(func):
    print 'Get in decorator_a'
    def inner_a(*args, **kwargs):
        print 'Get in inner_a'
        return func(*args, **kwargs)
    return inner_a

@decorator_a
def f(x):
    print 'Get in f'
    return x * 2

# 相当于
# def f(x):
#     print 'Get in f'
#     return x * 2
# f = decorator_a(f)

print f
'''
igis_gzy@CT-032515265640 MINGW64 /e/python/python-test/test (master)
$ python test18.py
Get in decorator_a
'''

