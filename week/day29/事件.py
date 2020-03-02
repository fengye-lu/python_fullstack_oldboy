# -*- coding: utf-8 -*-
# @Time    : 2020/3/2 12:49
# @Author  : Jackey-lu
# @File    : 事件.py

import threading, time

class Boss(threading.Thread):
    def run(self) -> None:
        print('boss：今晚大家都要加班到22:00。')
        event.isSet() or event.set()
        time.sleep(5)
        print("boss：<22:00>可以下班了。")
        event.isSet() or event.set()

class Worker(threading.Thread):
    def run(self) -> None:
        event.wait()
        print('worker: busy day')
        time.sleep(0.25)
        event.clear()
        event.wait()
        print('worker: happy!')

if __name__ == '__main__':
    event = threading.Event()
    threads = []
    for i in range(5):
        threads.append(Worker())
    threads.append(Boss())
    for t in threads:
        t.start()
    for t in threads:
        t.join()