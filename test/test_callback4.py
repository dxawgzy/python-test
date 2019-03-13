#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'igis_gzy'

def my_callback(input):
    print "function my_callback was called with %s input" % (input,)

def caller(input, func):
    func(input)

for i in range(5):
    caller(i, my_callback)


'''
执行结果如下：
igis_gzy@CT-032515265640 MINGW64 /e/python/python-test/test (master)
$ python test_callback4.py
function my_callback was called with 0 input
function my_callback was called with 1 input
function my_callback was called with 2 input
function my_callback was called with 3 input
function my_callback was called with 4 input

程序举例：引用 https://www.cnblogs.com/berlin-sun/p/callbackinpython.html 的内容。

关键代码是caller部分，将传入参数作为另外一个函数的定义。

另外：在知乎上看到一篇文章写得非常通俗易懂：
传送门：https://www.zhihu.com/question/19801131

作者：天涯海阁未走远
来源：CSDN
原文：https://blog.csdn.net/qq_21210467/article/details/80706277
'''
