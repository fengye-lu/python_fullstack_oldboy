# -*- coding: utf-8 -*-
# @Time    : 2020/2/27 18:32
# @Author  : Jackey-lu
# @File    : 单例模式.py

'''

class Foo:
    def __init__(self,name,age):
        self.name = name
        self.age = age

# obj = Foo() obj对象，obj也成为Foo类的实例，（实例化）
obj1 = Foo()
obj2 = Foo()
obj3 = Foo()
'''

'''
class Foo:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def show(self):
        print(self.name,self.age)

v = None
while True:
    if v :
        v.show()
    else:
        v = Foo('fengye',18)
        v.show()
'''


class Foo:
    __v = None

    @classmethod
    def get_instance(cls):
        if cls.__v:
            return cls.__v
        else:
            cls.__v = Foo()
            return cls.__v

# 不要再使用类()
obj1 = Foo.get_instance()
print(obj1)
obj2 = Foo.get_instance()
print(obj2)
obj3 = Foo.get_instance()
print(obj3)


