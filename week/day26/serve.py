# -*- coding: utf-8 -*-
# @Time    : 2020/2/28 14:25
# @Author  : Jackey-lu
# @File    : serve.py

'''
网络通信三要素
1. ip地址
2. 端口号
3. 传输协议
'''

'''
传输协议分为TCP和UDP
UDP传输速度快，但是不可靠，不安全，面向无连接（传输数据之前源端和目的端不需要建立连接）
每个数据报的大小都限制在64k（8个字节）以内。
现实生活实例：邮局寄件、实时在线聊天、视频会议等。
TCP是面向连接，通过三次握手完成连接，是安全可靠的，进行大量数据传输
'''


import socket

sk = socket.socket()    # family=AF_INET, type=SOCK_STREAM socket中的两个参数，
# family表示ipv6/ipv4，type表示传输协议，SOCK_STREAM表示的就是TCP协议

address = ('127.0.0.1',8000)

sk.bind(address)

sk.listen(3)  # 设置的是排队的个数
print('waiting.......')
conn,addr = sk.accept()
# print(conn)

inp = bytes(input('>>>>'),'utf8')
conn.send(inp)