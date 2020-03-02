# -*- coding: utf-8 -*-
# @Time    : 2020/3/1 17:04
# @Author  : Jackey-lu
# @File    : 信号量.py

import threading, time

class myThread(threading.Thread):
    def run(self) -> None:
        if semaphore.acquire():
            print(self.name)
            time.sleep(3)
            semaphore.release()

if __name__ == '__main__':
    semaphore = threading.BoundedSemaphore(5)  # 创建信号量锁对象
    thrs = []
    for i in range(100):
        thrs.append(myThread())
    for t in thrs:
        t.start()