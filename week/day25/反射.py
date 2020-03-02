# -*- coding: utf-8 -*-
# @Time    : 2020/2/27 16:40
# @Author  : Jackey-lu
# @File    : 反射.py


class Foo:
    def __init__(self,name,age):
        self.name = name
        self.age = age

obj = Foo('alex',18)
'''
obj.name
b = 'name'
obj.b  # obj.name
'''
# v = obj.__dict__('name')
# print(v)



#  通过字符串的形式操作对象中的成员
'''
inp = input('>>>')
v = getattr(obj,inp)  # 去什么里面获取什么内容
print(v)

print(hasattr(obj,'name'))  # 判断什么里面有没有什么

# obj.k
setattr(obj,'k1','v1')
print(obj.k1)

# obj.name
delattr(obj,'name')
obj.name

'''