# -*- coding: utf-8 -*-
# @Time    : 2020/2/23 14:12
# @Author  : Jackey-lu
# @File    : account_sample.py

import json

acc_dic = {
    'id':1234,
    'password':'abc',
    'credit':15000,
    'balance':15000,
    'enroll_date':'2016-01-02',
    'expire_date':'2021-01-01',
    'pay_day':22,
    'status':0
}
print(json.dumps(acc_dic))
info = json.dumps(acc_dic)

f = open('account/1234.json', 'w')
f.write(info)
f.close()

f = open('account/1234.json', 'r')
info = f.read()
info = json.loads(info)

print(info['balance'])