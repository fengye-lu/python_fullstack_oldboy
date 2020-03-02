# -*- coding: utf-8 -*-
# @Time    : 2020/3/1 18:32
# @Author  : Jackey-lu
# @File    : 队列.py

import queue

d = queue.Queue(3)

d.put('jinxin')  # 插入数据
d.put('xiaohu')
d.put('haoran',1)

# FIFO
print(d.get())
print(d.get())
print(d.empty())

print(d.queue)