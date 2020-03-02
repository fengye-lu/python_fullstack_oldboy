# -*- coding: utf-8 -*-
# @Time    : 2020/3/1 15:51
# @Author  : Jackey-lu
# @File    : 同步锁.py

import threading, time

def addNum():
    global num

    r.acquire()  # 获得锁
    temp = num
    time.sleep(0.000001)
    num = temp - 1
    r.release()   # 释放锁

num = 100
thread_list = []
r = threading.Lock()

for i in range(100):
    th = threading.Thread(target=addNum)
    th.start()
    thread_list.append(th)

for t in thread_list:
    t.join()

print('final num:', num)