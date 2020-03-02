# -*- coding: utf-8 -*-
# @Time    : 2020/2/27 12:58
# @Author  : Jackey-lu
# @File    : 成员修饰符.py

# class foo:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#         self.__age = age  # 私有，外部无法直接访问
#
#     def show(self):
#         return self.__age
#
#
# obj = foo('fengye',18)
# print(obj.name)
# print(obj.age)
# # print(obj.__age)
# print(obj.show())  # 可以间接调出私有字段的值


# class Foo:
# #     __v = '2323'
# #     def __init__(self):
# #         pass
# #
# #     def spy(self):
# #         return Foo.__v
# #
# #     @staticmethod
# #     def staticclass():
# #         return Foo.__v
# #
# # obj = Foo()
# # print(obj.spy())
# # print(obj.staticclass())


class foo:
    def __f1(self):  # 私有方法
        return 'ddd'
    def f2(self):
        rel = self.__f1()
        return rel

obj = foo()

# print(obj.__f1)
print(obj.f2())
