# -*- coding: utf-8 -*-
# @Time    : 2020/2/29 14:19
# @Author  : Jackey-lu
# @File    : lesson_threading.py

import time
import threading

# python中存在的GIL（全局解释器锁）问题：在同一时刻只能有一个线程进入解释器

'''
# I/O密集型任务或函数

start = time.time()
def foo(n):
    print('foo%s'%n)
    time.sleep(1)
    print('end foo')

def bar(n):
    print('bar%s'%n)
    time.sleep(2)
    print('end bar')

t1 = threading.Thread(target=foo,args=(1,))

t2 = threading.Thread(target=bar,args=(2,))
t1.start()
t2.start()

print('....in the main....')

t1.join()
t2.join()  # t1.join()表示如果t1没有执行完就不往下执行了

end = time.time()
print(end - start)
'''



'''
# 计算密集型任务或函数
start = time.time()
def add(n):
    sum = 0
    for i in range(n):
        sum += i
    print(sum)
    
add(10000)
add(20000)

t1 = threading.Thread(target=add,args=(10000,))

t2 = threading.Thread(target=add,args=(20000,))
t1.start()
t2.start()

t1.join()
t2.join()  # t1.join()表示如果t1没有执行完就不往下执行了

end = time.time()
print(end - start)
'''



