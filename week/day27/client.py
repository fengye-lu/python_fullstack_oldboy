# -*- coding: utf-8 -*-
# @Time    : 2020/2/29 12:48
# @Author  : Jackey-lu
# @File    : client.py

import socket

ip_port = ('127.0.0.1',8091)
sk = socket.socket()
sk.connect(ip_port)
print('客户端启动....')

while True:
    inp = input('>>>')
    sk.sendall(bytes(inp,'utf8'))
    if inp == 'exit':
        break
    server_reponse = sk.recv(1024)
    print(str(server_reponse,'utf8'))