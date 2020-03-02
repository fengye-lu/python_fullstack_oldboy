# -*- coding: utf-8 -*-
# @Time    : 2020/2/29 15:35
# @Author  : Jackey-lu
# @File    : threading_test.py

import threading
from time import ctime, sleep

# def music(func):
#     for i in range(2):
#         print('I was listening to %s. %s'%(func,ctime()))
#         sleep(1)
#
# def move(func):
#     for i in range(2):
#         print('I was at the %s! %s'%(func,ctime()))
#         sleep(5)
#
# if __name__ == '__main__':
#     music('七里香')
#     move('世界末路')


def music(func):
    print(threading.current_thread())
    for i in range(2):
        print('I was listening to %s. %s' % (func, ctime()))
        sleep(1)
        print('end listening %s'%ctime())


def move(func):
    print(threading.current_thread())
    for i in range(2):
        print('I was watching the %s! %s' % (func, ctime()))
        sleep(5)
        print('end watching %s'%ctime())

threads = []
t1 = threading.Thread(target=music,args=('七里香',))
threads.append(t1)
t2 = threading.Thread(target=move,args=('世界末路',))
threads.append(t2)

if __name__ == '__main__':
    t1.setDaemon(True)
    for t in threads:
        # t.setDaemon(True)  # 守护线程(其他线程一旦结束，守护线程也会立马结束)
        t.start()

    t.join()
    print(threading.current_thread())
    print('all over %s'%ctime())
