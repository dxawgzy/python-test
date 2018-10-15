#coding=utf-8
#!/usr/bin/env python
__author__ = 'igis_gzy'

# class Next:
#   List = []
#
#   def __init__(self,low,high) :
#     for Num in range(low,high) :
#       self.List.append(Num ** 2)
#
#   def __call__(self,Nu):
#     return self.List[Nu]
#
# if __name__ == '__main__':
#     b = Next(1,7)
#     print b.List
#     print b(2)    #此处使用了__call__方法
    # 返回结果：
    # [1, 4, 9, 16, 25, 36]
    # 9
    # 若注释掉__call__方法，则执行此处会报错：
    # Traceback (most recent call last):
    # [1, 4, 9, 16, 25, 36]
    #   File "E:/python/python-test/test/test_call.py", line 18, in <module>
    #     print b(2)
    # AttributeError: Next instance has no __call__ method

    # b = Next
    # b(1,7)
    # print b.List
    # print b(2)
    # 执行结果如下：
    # Traceback (most recent call last):
    # [1, 4, 9, 16, 25, 36]
    #   File "E:/python/python-test/test/test_call.py", line 21, in <module>
    #     print b(2)
    # TypeError: __init__() takes exactly 3 arguments (2 given)
    # __init__是初始化函数，在生成类的实例时执行。
    # 而__call__是模拟()的调用，需要在实例上应用，因此这个实例自然是已经执行过__init__了。
    #
    # 所举的后面那个例子：
    # b = Next
    #
    # 这并不是创建实例，而是将class赋给一个变量。因此后面使用b进行的操作都是对Next类的操作，那么其实就是：
    # Next(1,7)
    # print Next.List
    # print Next(2)



# 对象通过提供__call__(self, [,*args [,**kwargs]])方法可以模拟函数的行为，如果一个对象x提供了该方法，
# 就可以像函数一样使用它，也就是说x(arg1, arg2...) 等同于调用x.__call__(self, arg1, arg2)。
# 模拟函数的对象可以用于创建仿函数(functor) 或代理(proxy)
#
# class DistanceForm(object):
#   def __init__(self, origin):
#     self.origin = origin
#     print "origin :"+str(origin)
#   def __call__(self, x):
#     print "x :"+str(x)
# p = DistanceForm(100)
# p(2000)
#
# 输出：
# origin :100
# x :2000



class Animal(object):
    def __init__(self, name, legs):
        self.name = name
        self.legs = legs
        self.stomach = []

    def __call__(self,food):
        self.stomach.append(food)

    def poop(self):
        if len(self.stomach) > 0:
            return self.stomach.pop(0)

    def __str__(self):
        return 'A animal named %s' % (self.name)

cow = Animal('king', 4)  #We make a cow
dog = Animal('flopp', 4) #We can make many animals
print 'We have 2 animales a cow name %s and dog named %s,both have %s legs' % (cow.name, dog.name, cow.legs)
print cow  #here __str__ metod work

#We give food to cow
cow('gras')
print cow.stomach

#We give food to dog
dog('bone')
dog('beef')
print dog.stomach

#What comes inn most come out
print cow.poop()
print cow.stomach  #Empty stomach

'''-->output
We have 2 animales a cow name king and dog named flopp,both have 4 legs
A animal named king
['gras']
['bone', 'beef']
gras
[]
'''

