# -*- coding: utf-8 -*-
# @Time    : 2020/3/1 16:15
# @Author  : Jackey-lu
# @File    : 死锁和递归锁.py

import threading, time

'''
class myThread(threading.Thread):
    def doA(self):
        lockA.acquire()
        print(self.name,'gotlockA',time.ctime())
        time.sleep(3)
        lockB.acquire()
        print(self.name,'gotlockB',time.ctime())
        lockB.release()
        lockA.release()

    def doB(self):
        lockB.acquire()
        print(self.name,'gotlockB',time.ctime())
        time.sleep(2)
        lockA.acquire()
        print(self.name, 'gotlockA', time.ctime())
        lockA.release()
        lockB.release()

    def run(self):
        self.doA()
        self.doB()

if __name__ == '__main__':
    lockA = threading.Lock()
    lockB = threading.Lock()
    threads = []

    for i in range(5):
        threads.append(myThread())
    for t in threads:
        t.start()
    for t in threads:
        t.join()
'''


class myThread(threading.Thread):
    def doA(self):
        lock.acquire()
        print(self.name,'gotlockA',time.ctime())
        time.sleep(3)
        lock.acquire()
        print(self.name,'gotlockB',time.ctime())
        lock.release()
        lock.release()

    def doB(self):
        lock.acquire()
        print(self.name,'gotlockB',time.ctime())
        time.sleep(2)
        lock.acquire()
        print(self.name, 'gotlockA', time.ctime())
        lock.release()
        lock.release()

    def run(self):
        self.doA()
        self.doB()

if __name__ == '__main__':
    # lockA = threading.Lock()
    # lockB = threading.Lock()
    lock = threading.RLock()
    threads = []

    for i in range(5):
        threads.append(myThread())
    for t in threads:
        t.start()
    for t in threads:
        t.join()


