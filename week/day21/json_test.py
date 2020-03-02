# -*- coding: utf-8 -*-
# @Time    : 2020/2/22 15:10
# @Author  : Jackey-lu
# @File    : json_test.py

import json

dic = {'name':'alex','age':'18'}

f = open('JSON_test','w')

# date = json.dumps(dic)
# f.write(date)
data = json.dump(dic,f)
f.close()