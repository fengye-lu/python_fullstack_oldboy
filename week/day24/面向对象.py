# -*- coding: utf-8 -*-
# @Time    : 2020/2/25 12:05
# @Author  : Jackey-lu
# @File    : 面向对象.py

'''
如果多个函数中有一些相同的参数时，转换成面向对象
'''
# class test:
#     def test(self,arg):
#         print(arg)
#         return 3
#
# obj = test()  # obj这个中间人就是对象
#
# result = obj.test('\033[33;1mhello world!\033[0m')
# print(result)


'''
封装特性，把数据封装到对象中
'''
# class Bar:
#     def add(self,content):
#         print(self.name,self.age,self.gender,content)
#
#     def delete(self,content):
#         print(self.name,self.age,self.gender,content)
#
#     def update(self,content):
#         print(self.name,self.age,self.gender,content)
#
#     def select(self,content):
#         print(self.name,self.age,self.gender,content)
#
# obj = Bar()
# obj.name = '小明'
# obj.age = 13
# obj.gender = 'male'
#
# obj.add('上山去砍柴')
# obj.delete('开车去东北')
# obj.update('好好学习')
# obj.select('天天向上')


'''
构造方法，根据构造方法将值封装到对象当中
'''
# class Bar:
#     def __init__(self, name, age, gender):   # 构造方法
#         '''
#         类名（）自动执行构造方法
#         :param name:
#         :param age:
#         :param gender:
#         '''
#
#         self.name = name
#         self.age = age
#         self.gender = gender
#
#     def add(self, content):
#         print(self.name, self.age, self.gender, content)
#
#     def delete(self, content):
#         print(self.name, self.age, self.gender, content)
#
#     def update(self, content):
#         print(self.name, self.age, self.gender, content)
#
#     def select(self, content):
#         print(self.name, self.age, self.gender, content)
#
# obj = Bar('小明', 13, 'male')
#
# obj.add('上山去砍柴')
# obj.delete('开车去东北')
# obj.update('好好学习')
# obj.select('天天向上')


'''
继承
'''

# class Father:   # 父类， 基类
#     def basktball(self):
#         pass
#     def football(self):
#         pass
#     def sing(self):
#         print('I like singing!')
#     def drink(self):
#         print('ni hao!')
#
# class Son(Father):   # 子类, 派生类
#     def volleyball(self):
#         pass
#
#     def drink(self):    # 重写drink方法
#         super(Son,self).drink()  # 执行父类中的drink()方法
#         # Father.drink(self)  # 执行父类中的drink()的第二种方法
#         print('I like drinking!')
#
# obj = Son()
# obj.sing()
# obj.drink()

# 多继承
# class F_1:
#     def a(self):
#         print('F_1.a')
# class F0(F_1):
#     def a2(self):
#         print('F0.a')
# class F1(F0):
#     def a1(self):
#         print('F1.a')
# class F2:
#     def a(self):
#         print('F2.a')
#
# class f(F1, F2):
#     pass
#
# obj = f()
# obj.a()


'''
静态方法，类方法
'''
class foo:
#     def f1(self):
#         pass
#
#     @staticmethod
#     def f2():
#         print('静态方法')
#
    @classmethod
    def f3(self):
        # self 此时表示当前的类名
        print(self)
        print('类方法')
#
    @property
    def f4(self):
        print('定义时像方法，调用时像字段')
        return 2
    @f4.setter
    def f4(self,val):
        print(val)
#     @f4.deleter
#     def f4(self):
#         print(666)
#
# foo.f2()
foo.f3()
#
object = foo()
# val = object.f4
# print(val)
object.f4 = 123456   # 对应的是@f4.setter
# del object.f4    # 对应的是@f4.deleter


# class Pergination:
#     def __init__(self,current_page):
#         try:
#             p = int(current_page)
#         except Exception as e:
#             p = 1
#
#         self.page = p
#     @property
#     def start(self):
#         val = (self.page-1)*10
#         return val
#     @property
#     def end(self):
#         val = self.page*10
#         return val
#
# li = []
# for i in range(1000):
#     li.append(i)
#
# while True:
#     p = input('请输入要查看的页码：')
#     obj = Pergination(p)
#     print(li[obj.start:obj.end])
