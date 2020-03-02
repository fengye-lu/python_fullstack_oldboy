# -*- coding: utf-8 -*-
# @Time    : 2020/2/15 12:20
# @Author  : Jackey-lu
# @File    : 函数的作用域.py

count = 10

def change():
    # count = count +1
    count = 1


def outer():
    count = 10
    def inner():
        nonlocal count
        count = 20
        print(count)
    inner()
    print(count)

outer()