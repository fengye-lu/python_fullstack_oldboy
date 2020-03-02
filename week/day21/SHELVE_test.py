# -*- coding: utf-8 -*-
# @Time    : 2020/2/22 19:19
# @Author  : Jackey-lu
# @File    : SHELVE_test.py

import shelve

f = shelve.open('SHELVE_test')

f['info'] = {'name':'alex','age':'18'}

data = f.get('info')
print(data)