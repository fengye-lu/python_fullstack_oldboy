# -*- coding: utf-8 -*-
# @Time    : 2020/2/23 19:37
# @Author  : Jackey-lu
# @File    : transaction.py

from conf import settings
from core import accounts

def make_transaction(log_obj,account_data,tran_type,amount,**others):
    amount = float(amount)
    if tran_type in settings.TRANSACTION_TYPE:
        interest = amount * settings.TRANSACTION_TYPE[tran_type]['interest']
        old_balance = account_data['balance']
        if settings.TRANSACTION_TYPE[tran_type]['action'] == 'plus':
            new_balance = old_balance+amount+interest
        elif settings.TRANSACTION_TYPE[tran_type]['action'] == 'minus':
            new_balance = old_balance - amount -interest
            if new_balance < 0 :
                print('''\033[31;1mYour credit [%s] is not enough for this transaction'''%account_data['credit'])
                return

        account_data['balance'] = new_balance
        accounts.dump_account(account_data)
        log_obj.info('account:%s action:%s amount:%s interest:%s'%
                     (account_data['id'],tran_type,amount,interest))
        return account_data
    else:
        print('\033[31;1mTransaction type [%s] is not exist!\033[0m'%tran_type)