# -*- coding: utf-8 -*-
# @Time    : 2020/2/22 18:52
# @Author  : Jackey-lu
# @File    : pickle_test.py

import pickle

def foo():
    print('ni hao')

news = pickle.dumps(foo)
f = open('PICKLE_test','wb')

f.write(news)
f.close()