#!/usr/bin/python

def deco_functionNeedDoc(func):
    if func.__doc__ == None :
        print func, "has no __doc__, it's a bad habit."
    else:
        print func, ':', func.__doc__, '.'
    return func

@deco_functionNeedDoc
def f():
    print 'f() Do something'

@deco_functionNeedDoc
def g():
    'I have a __doc__'
    print 'g() Do something'
f()
g()

'''
igis_gzy@CT-032515265640 MINGW64 /e/python/python-test/test (master)
$ python test24.py
<function f at 0x00000000026639E8> has no __doc__, it's a bad habit.
<function g at 0x0000000002663A58> : I have a __doc__ .
f() Do something
g() Do something
'''
