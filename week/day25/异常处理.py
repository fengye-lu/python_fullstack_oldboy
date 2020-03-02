# -*- coding: utf-8 -*-
# @Time    : 2020/2/27 16:03
# @Author  : Jackey-lu
# @File    : 异常处理.py

'''
try:
    # 代码块
    pass
except IndexError as e:
    print('IndexError',e)
except ValueError as e:
    print('ValueError',e)
except Exception as e:
    # 上述代码块如果出错，则自动执行当前块内容
    # e 是Exception的对象，对象中封装了错误信息
    print('Exception',e)
else:
    print('elese') # 如果没有错误会执行这个代码块
finally:
    print('.....') # 无论有没有错误都会执行这个代码块
'''





'''
try:
    raise Exception('不过了。。。')   # 主动发出异常
except Exception as e:
    print(e)
'''


'''
# 自定义异常
class OldBoyError(Exception):
    def __init__(self,msg):
        self.message = msg

    def __str__(self):
        return self.message

try:
    raise OldBoyError('我错了。。。。。')
except OldBoyError as e:
    print(e)
'''



'''
# assert 条件（断言），用于强制用户服从，不服从就报错，可补货，一般不补货
# 条件成立通过，条件不成立报错
'''