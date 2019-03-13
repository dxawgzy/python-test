#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'igis_gzy'

def deco_functionNeedDoc(func1):
    if func1.__name__ == "yyy" :
        print func1, "the func1 == yyy"
    else:
        print func1, ':', func1.__doc__, '.'

    def xxx() : # y + f + h + x
        func1() # y + f + h + f + h
        print "plus xxx"
        return func1() # y + f + h + f + h

    return xxx

def deco_functionNeedDocxxx(func2):
    if func2.__name__ == "hhh" :
        print func2, "the func2 == hhh"
    else:
        print func2, ':', func2.__doc__, '.'

    def yyy(): # y + f + h + f + h
        print "plus yyy"
        func2()  # f + h
        return func2() # f + h

    return yyy

def deco_functionNeedDochhh(func3):
    if func3.__name__ == "f" :
        print func3, "the func3 == f"
    else:
        print func3, ':', func3.__doc__, '.'

    def hhh() : # = f + h
        func3()  # = f
        print "plus hhh"
        return "Hello World"
    return hhh


@deco_functionNeedDoc
@deco_functionNeedDocxxx
@deco_functionNeedDochhh
def f():
    print 'print original fff'

f()
print "------------"
print f
print "------------"
print f()


'''
igis_gzy@CT-032515265640 MINGW64 /e/python/python-test/test (master)
$ python test17.py
<function f at 0x00000000026B3AC8> the func3 == f
<function hhh at 0x00000000026B3B38> the func2 == hhh
<function yyy at 0x00000000026B3BA8> the func1 == yyy
plus yyy
print original fff
plus hhh
print original fff
plus hhh
plus xxx
plus yyy
print original fff
plus hhh
print original fff
plus hhh
------------
<function xxx at 0x00000000026B3C18>
------------
plus yyy
print original fff
plus hhh
print original fff
plus hhh
plus xxx
plus yyy
print original fff
plus hhh
print original fff
plus hhh
Hello World
'''
