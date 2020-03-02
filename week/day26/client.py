# -*- coding: utf-8 -*-
# @Time    : 2020/2/28 14:26
# @Author  : Jackey-lu
# @File    : client.py

import socket

sk = socket.socket()

address = ('127.0.0.1',8000)

sk.connect(address)

data = sk.recv(1024)

print(str(data,'utf8'))