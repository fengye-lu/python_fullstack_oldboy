# -*- coding: utf-8 -*-
# @Time    : 2020/2/17 13:16
# @Author  : Jackey-lu
# @File    : hashlib模块.py

import hashlib

m = hashlib.md5()
print(m)
m.update('hello world!'.encode('utf8'))
print(m.hexdigest())
m.update('lzh'.encode('utf8'))
print(m.hexdigest())

s = hashlib.sha256()
s.update('hello world!'.encode('utf8'))
print(s.hexdigest())