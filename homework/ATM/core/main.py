# -*- coding: utf-8 -*-
# @Time    : 2020/2/23 14:06
# @Author  : Jackey-lu
# @File    : main.py
from core import logger,accounts
from core import transaction
from core import auth
import time
import json
from bin.atm import base_dir

trans_logger = logger.logger('transaction')
access_logger = logger.logger('access')

user_data = {
    'account_id':None,
    'is_authenticated':False,
    'account_data':None
}


def account_info(acc_data):
    print(user_data)

def repay(acc_data):
    account_data = accounts.load_current_balance(acc_data['account_id'])

    current_balance='''------BALANCE INFO------
        Credit :  %s
        Balance:  %s
    '''%(account_data['credit'],account_data['balance'])
    print(current_balance)
    back_flag = False
    while not back_flag:
        repay_amount = input('\033[33;1mInput repay amount:\033[0m').strip()
        if len(repay_amount) > 0 and repay_amount.isdigit():
            print('ddd 00')
            new_balance = transaction.make_transaction(trans_logger, account_data, 'repay', repay_amount)
            if new_balance:
                print('''\033[42;1mNew Balance:%s\033[0m'''%(new_balance['balance']))
            else:
                print('\033[31;1m[%s] is not a valid amount, only accept integer!\033[0m'%repay_amount)
        elif repay_amount =='back':
            back_flag = True

def withdraw(acc_data):
    account_data = accounts.load_current_balance(acc_data['account_id'])

    current_balance = '''------BALANCE INFO------
        Credit :  %s
        Balance:  %s
    ''' % (account_data['credit'], account_data['balance'])
    print(current_balance)
    back_flag = False
    while not back_flag:
        withdraw_amount = input('\033[33;1mInput withdraw amount:\033[0m').strip()
        if len(withdraw_amount) > 0 and withdraw_amount.isdigit():
            new_balance = transaction.make_transaction(trans_logger, account_data, 'withdraw', withdraw_amount)
            if new_balance:
                print('''\033[42;1mNew Balance:%s\033[0m''' % (new_balance['balance']))
            else:
                print('\033[31;1m[%s] is not a valid amount, only accept integer!\033[0m' % withdraw_amount)
        break

def transfer():
    pass

def pay_check():
    pass

def logout(acc_data):
    print('\033[32;1mI HOPE SEE YOU AGAIN!\033[0m'.center(10))
    exit()

def regisit(acc_data):
    id = input('\033[32;1mregisit account:\033[0m').strip()
    password = input('\033[32;1mpassword:\033[0m').strip()
    credit = input('\033[32;1mmoney amount:\033[0m').strip()
    balance = credit
    enroll_date = time.ctime()
    expire_date = "2021-01-01"
    acc_dic = {
        'id': id,
        'password': password,
        'credit': credit,
        'balance': balance,
        'enroll_date': enroll_date,
        'expire_date': expire_date,
        'pay_day': 22,
        'status': 0
    }
    info = json.dumps(acc_dic)
    with open('%s/db/account/%s.json'%(base_dir, id), 'w') as f:
        f.write(info)



def interactive(acc_data):
    menu = u'''
    ------fengye Bank------
    \033[32;1m1.  账户信息
    2.  还款
    3.  取款
    4.  转账
    5.  账单
    6.  退出
    7.  注册
    \033[0m
    '''
    menu_dic = {
        '1': account_info,
        '2': repay,
        '3': withdraw,
        '4': transfer,
        '5': pay_check,
        '6': logout,
        '7': regisit
    }
    exit_flag = False
    while not exit_flag:
        print(menu)
        user_option = input('>>:').strip()
        if user_option in menu_dic:
            menu_dic[user_option](acc_data)

        else:
            print('\033[31;1mOption dose not exit!\033[0m')

def run():
    acc_data = auth.acc_login(user_data, access_logger)

    if user_data['is_authenticated']:
        user_data['account_data'] =acc_data
        interactive(user_data)