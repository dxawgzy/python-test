#!/usr/bin/python
#coding=utf-8

def decomaker(arg):  
#    '通常对arg会有一定的要求'  
    """由于有参数的decorator函数在调用时只会使用应用时的参数  
       而不接收被装饰的函数做为参数，所以必须在其内部再创建  
       一个函数  
    """

    def newDeco(func):    #定义一个新的decorator函数  
        print func, arg  
        return func  
    return newDeco  

@decomaker(deco_args)  
def foo():pass  
foo() 



