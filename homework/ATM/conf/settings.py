# -*- coding: utf-8 -*-
# @Time    : 2020/2/23 14:34
# @Author  : Jackey-lu
# @File    : settings.py

import os
import logging

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


DATABASE = {
    'engine': 'file_storage',
    'name': 'account',
    'path': '%s/db' % BASE_DIR
}

LOG_LEVEL = logging.INFO
LOG_TYPES ={
    'transaction': 'transactions.log',
    'access': 'access.log'
}


TRANSACTION_TYPE = {
    'repay':{'action':'plus','interest':0},
    'withdraw':{'action':'minus','interest':0.05},
    'transfer':{'action':'minus','interest':0.05},
    'consume':{'action':'minus','interest':0}
}