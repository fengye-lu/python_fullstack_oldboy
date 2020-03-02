# -*- coding: utf-8 -*-
# @Time    : 2020/2/15 13:55
# @Author  : Jackey-lu
# @File    : 递归.py
z = 1
def comput(x):
    global z
    z *= x
    x -= 1
    while x > 0:
        comput(x)
        return z

print(comput(5))