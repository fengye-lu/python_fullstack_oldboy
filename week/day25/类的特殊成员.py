# -*- coding: utf-8 -*-
# @Time    : 2020/2/27 13:59
# @Author  : Jackey-lu
# @File    : 类的特殊成员.py

# class foo:
#     def __init__(self):
#         print('init')
#
#     def __call__(self, *args, **kwargs):
#         print('call')
#
#     def __del__(self):
#         print('析构方法')  # 对象被销毁时，自动执行
#
# obj = foo()   # 自动执行__init__方法（python自己规定的）
# obj()  # 自动执行__call__方法 （python自己规定的）
# foo()()

'''
def __int__():  int(对象)
def __str__():  str()
def __init__():
def __call__():
__dict__  # 将对象中封装的所有内容通过字典的形式返回
'''


# class foo:
#     def __init__(self,name,age,sex):
#         self.name = name
#         self.age = age
#         self.sex = sex
#
# obj = foo('fengye',12,'male')
# str = obj.__dict__
# print(str)


# li = [11,22,33,44]
# del li[2]
# li.remove(11)
# ret = li.pop(0)
# print(li,ret)

class Foo:

    def __init__(self):
        pass

    def __getitem__(self, item):
        return item+10

    def __setitem__(self, key, value):
        print(key,value)

    def __delitem__(self, key):
        print(key)

li = Foo()
r = li[8]
print(r)

li[100] = 'asad'
del li[999]