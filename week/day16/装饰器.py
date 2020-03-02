# -*- coding: utf-8 -*-
# @Time    : 2020/2/25 18:01
# @Author  : Jackey-lu
# @File    : 装饰器.py

import time

# def show_time(f):    # 装饰器函数
#     def inner():
#         start = time.time()
#         f()
#         end = time.time()
#         print('spend %s'%(end-start))
#     return inner
#
# @show_time    # 相当于foo = show_time(foo)
# def foo():
#     print('foo....')
#     time.sleep(2)

# @show_time
# def bar():
#     print('bar....')
#     time.sleep(3)

# foo = show_time(foo)
# foo()





# 功能函数加参数
# def show_time(f):    # 装饰器函数
#     def inner(a,b):
#         start = time.time()
#         f(a,b)
#         end = time.time()
#         print('spend %s'%(end-start))
#     return inner
#
# @show_time    # 相当于foo = show_time(foo)
# def add(a,b):
#     print(a+b)
#     time.sleep(2)
#
# add(1,2)




# 装饰器加参数
def logger(Flag):
    def show_time(f):    # 装饰器函数
        def inner():
            start = time.time()
            f()
            end = time.time()
            print('spend %s'%(end-start))
            if Flag == 'true':
                print('日志记录')
            else:
                print('不记录日志')
        return inner
    return show_time

@logger('true')    # 相当于foo = show_time(foo)
def foo():
    print('foo....')
    time.sleep(2)

@logger('false')
def bar():
    print('bar....')
    time.sleep(3)

foo()
bar()