# -*- coding: utf-8 -*-
# @Time    : 2020/2/22 15:14
# @Author  : Jackey-lu
# @File    : JSON_loads.py

import json

f = open('JSON_test','r')

# data = f.read()
# data = json.loads(data)
data = json.load(f)

print(data['name'])