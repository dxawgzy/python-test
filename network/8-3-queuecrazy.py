#coding=utf8
__author__ = 'igis_gzy'   # P132
#!usr/bin/python

import random, threading, time, zmq
zcontext = zmq.Context()
# D:\python27\Lib\site-packages\zmq\sugar\context.py
# D:\python27\Lib\site-packages\zmq\backend\cffi\socket.py

def fountain(url):
    zsock = zcontext.socket(zmq.PUSH)
    """ def socket(self, socket_type):
        Create a Socket associated with this Context.
        The socket type, which can be any of the 0MQ socket types:
        REQ, REP, PUB, SUB, PAIR, DEALER, ROUTER, PULL, PUSH, etc.
    """
    zsock.bind(url)
    words = [w for w in dir(__builtins__) if w.islower()]
    # dir(__builtins__)  dir()内置函数,列出一个定义对象的标识符。例如，对于一个模块，包括在模块中定义的函数，类和变量。
    # 直接命令行执行这条命令会有输出
    # S.islower()  Return True if all cased characters in S are lowercase(小写字母).
    while True:
        zsock.send(random.choice(words))
        # random.choice(seq)  Choose a random element from a non-empty sequence.
        time.sleep(0.4)

def responder(url, function):   # 函数名作为函数的参数
    zsock = zcontext.socket(zmq.REP)
    zsock.bind(url)
    while True:
        word = zsock.recv()
        zsock.send(function(word))

def processor(n, fountain_url, responder_urls):
    zpullsock = zcontext.socket(zmq.PULL)
    zpullsock.connect(fountain_url)

    zreqsock = zcontext.socket(zmq.REQ)
    for url in responder_urls:
        zreqsock.connect(url)

    while True:
        word = zpullsock.recv()
        zreqsock.send(word)
        print n, zreqsock.recv()

def start_thread(function, *args):   # 函数名作为函数的参数
    thread = threading.Thread(target=function, args=args)
    thread.daemon = True
    # A boolean value indicating whether this thread is a daemon thread (True) or not (False).
    # This must be set before start() is called, otherwise RuntimeError is raised.
    thread.start()
    # Start the thread's activity.It must be called at most once per thread object. It arranges for the
    # object's run() method to be invoked in a separate thread of control.

start_thread(fountain, 'tcp://127.0.0.1:6700')
start_thread(responder, 'tcp://127.0.0.1:6701', str.upper)
start_thread(responder, 'tcp://127.0.0.1:6702', str.lower)
# S.upper()  Return a copy of the string S converted to uppercase(大写字母).
# S.lower()  Return a copy of the string S converted to lowercase(小写字母).
for n in range(3):
    start_thread(processor, n + 1, 'tcp://127.0.0.1:6700',
                 ['tcp://127.0.0.1:6701', 'tcp://127.0.0.1:6702'])
time.sleep(30)


# pip install pyzmq-static



