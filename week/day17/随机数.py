# -*- coding: utf-8 -*-
# @Time    : 2020/2/16 15:30
# @Author  : Jackey-lu
# @File    : 随机数.py

import random

print(random.random())
print(random.randint(1, 9))
print(random.choice('hello'))
print(random.sample(['123', 2, 4, '212'], 2))
print(random.randrange(1, 9))

#  随机生成验证码
def val_code():
    code = ''
    for i in range(5):
        add = random.choice([random.randint(0, 9), chr(random.randint(65, 90))])
        code += str(add)
    return code
print(val_code())