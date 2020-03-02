# -*- coding: utf-8 -*-
# @Time    : 2020/2/22 18:55
# @Author  : Jackey-lu
# @File    : PICKLE_loads.py

import pickle

def foo():
    print('ni hao')

f = open('PICKLE_test','rb')
new = f.read()
new = pickle.loads(new)
new()