# -*- coding: utf-8 -*-
# @Time    : 2020/2/29 12:48
# @Author  : Jackey-lu
# @File    : serve.py

import socketserver

class MyServer(socketserver.BaseRequestHandler):
    def handle(self):
        print('服务器端启动....')
        while True:
            conn = self.request
            print(self.client_address)
            while True:
                client_data = conn.recv(1024)
                print(str(client_data,'utf8'))
                print('waiting...')
                server_response = input('>>>')
                conn.sendall(bytes(server_response,'utf8'))
            conn.close()

if __name__ =='__main__':
    server = socketserver.ThreadingTCPServer(('127.0.0.1',8091),MyServer)
    server.serve_forever()