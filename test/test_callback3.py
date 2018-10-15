#coding=utf-8
#!/usr/bin/env python
__author__ = 'igis_gzy'

class CallbackBase:
    def __init__(self):
        self.__callbackMap = {}
        print dir(self)
        for k in (getattr(self, x) for x in dir(self)):
            if hasattr(k, "bind_to_event"):
                self.__callbackMap.setdefault(k.bind_to_event, []).append(k)
            elif hasattr(k, "bind_to_event_list"):
                for j in k.bind_to_event_list:
                    self.__callbackMap.setdefault(j, []).append(k)
        print self.__callbackMap

    # staticmethod is only used to create a namespace
    @staticmethod
    def callback(event):
        def f(g, ev = event):
            g.bind_to_event = ev
            print g.bind_to_event
            return g
        return f

    @staticmethod
    def callbacklist(eventlist):
        def f(g, evl = eventlist):
            g.bind_to_event_list = evl
            print g.bind_to_event_list
            return g
        return f

    def dispatch(self, event):
        l = self.__callbackMap[event]
        f = lambda *args, **kargs: \
            map(lambda x: x(*args, **kargs), l)
        print l
        # print f
        return f

# Sample
class MyClass(CallbackBase):
    EVENT1 = 1
    EVENT2 = 2

    @CallbackBase.callback(EVENT1)
    def handler1(self, param = None):
        print "handler1 with param: %s" % str(param)
        return None

    @CallbackBase.callbacklist([EVENT1, EVENT2])
    def handler2(self, param = None):
        print "handler2 with param: %s" % str(param)
        return None

    def run(self, event, param = None):
        self.dispatch(event)(param)

if __name__ == "__main__":
    a = MyClass()
    a.run(MyClass.EVENT1, 'mandarina')  # a.run(1, 'mandarina')  self.dispatch(1)('mandarina')
    a.run(MyClass.EVENT2, 'naranja')

'''
E:\python\python-test\test>python test_callback3.py
handler1 with param: mandarina
handler2 with param: mandarina
handler2 with param: naranja
'''

'''

当你要加入回调（Callback）功能的时候，代码往往会偏重于回调的实现而不是问题本身了。
一个解决方法就是实现一个通用的基础类来解决回调的需求，然后再来实现你为某个事件（Event）所绑定（Binding）的方法（Method）

这里有一个类，它有两个事件（EVENT1和EVENT2）和两个处理函数（handler）。第一个处理函数handler1注册了EVENT1，
而第二个处理函数handler2当EVENT1或者EVENT2发生的时候都会执行（即注册了全部的事件）。

运行函数（run）在MyClass的主循环中，它会将对应的事件派送（dispatch）出去。这（这里指dispatch函数）会返回一个函数，
我们可以把所有需要传给这个函数的参数列表传给它。这个函数运行结束会返回一个列表（list），列表中是所有的返回值。


Python函数式编程之map()
python中map()、filter()、reduce()这三个都是应用于序列的内置函数。
格式：
map(func, seq1[, seq2,…])
第一个参数接受一个函数名，后面的参数接受一个或多个可迭代的序列，返回的是一个集合。
Python函数编程中的map()函数是将func作用于seq中的每一个元素，并将所有的调用的结果作为一个list返回。
#使用lambda
>>> print map(lambda x: x % 2, range(7))
[0, 1, 0, 1, 0, 1, 0]

>>> L = [1,2,3,4]
>>> print map((lambda x: x+10), L)
[11, 12, 13, 14]


Python 字典 setdefault() 函数和get() 方法类似, 如果键不存在于字典中，将会添加键并将值设为默认值。
setdefault()方法语法：
dict.setdefault(key, default=None)
参数
    key -- 查找的键值。
    default -- 键不存在时，设置的默认键值。
返回值
如果字典中包含有给定键，则返回该键对应的值，否则返回为该键设置的值。
实例
以下实例展示了 setdefault() 函数的使用方法：
实例(Python 2.0+)
#!/usr/bin/python
# -*- coding: UTF-8 -*-
dict = {'runoob': '菜鸟教程', 'google': 'Google 搜索'}
print "Value : %s" %  dict.setdefault('runoob', None)
print "Value : %s" %  dict.setdefault('Taobao', '淘宝')
以上实例输出结果为：
Value : 菜鸟教程
Value : 淘宝

'''

