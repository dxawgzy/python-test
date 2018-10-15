#coding=utf-8
#!/usr/bin/env python
__author__ = 'igis_gzy'

class Callback:
    def __init__(self, instance, function_name):
        self.instance = instance     # api.self
        self.function_name = function_name     # function

    def action(self, params):
        print self.instance.__getattribute__(self.function_name)
        self.instance.__getattribute__(self.function_name)(params)

class Test:
    def __init__(self):
        self.clb = None

    def register(self, clb):
        self.clb = clb     # Callback(self, self.function.__name__)

    def do_test(self):
        params = [1, 2]
        self.clb.action(params)

class Api(object):
    def __init__(self, test_instance):
        test_instance.register(Callback(self, self.function.__name__))

    def function(self, params):
        print params

t = Test()
a = Api(t)
t.do_test()


'''
E:\python\python-test\test>python test_callback.py
<bound method Api.function of <__main__.Api object at 0x00000000026CAFD0>>
[]
function
'''

