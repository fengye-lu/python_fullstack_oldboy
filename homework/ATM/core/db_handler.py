# -*- coding: utf-8 -*-
# @Time    : 2020/2/23 15:19
# @Author  : Jackey-lu
# @File    : db_handler.py

# 为了处理更多的数据存储情况设置的函数

def file_db_handle(conn_params):
    print('file db:',conn_params)
    db_path = '%s/%s'%(conn_params['path'],conn_params['name'])
    return db_path

def db_handler(conn_parms):
    if conn_parms['engine'] == 'file_storage':
        return file_db_handle(conn_parms)