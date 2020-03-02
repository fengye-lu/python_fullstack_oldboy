# -*- coding: utf-8 -*-
# @Time    : 2020/2/16 12:51
# @Author  : Jackey-lu
# @File    : 列表生成器.py

a = [x for x in range(10)]
print(a)


s = (x*2 for x in range(10))
print(s) # <generator object <genexpr> at 0x000001B2A17EFF10>
print(next(s))


# 生成器一共两种创建方式:
# 1. (x*2 for x in range(10))
# 2. yield

def foo():
    print('ok!')
    yield 1
    print('ok2!')
    yield 2

g = foo()
print(g)  # <generator object foo at 0x0000023585AC9BA0>

# next(g)
# next(g)
for i in foo():
    print(i)