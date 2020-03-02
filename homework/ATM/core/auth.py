# -*- coding: utf-8 -*-
# @Time    : 2020/2/23 15:03
# @Author  : Jackey-lu
# @File    : auth.py

import time
from core import db_handler
from conf import settings
import json,os

def acc_auth(account,password):

    db_path = db_handler.db_handler(settings.DATABASE)
    account_file = '%s/%s.json'%(db_path,account)
    print(account_file)
    if os.path.isfile(account_file):
        with open(account_file,'r') as f:
            account_data = json.load(f)
            if account_data['password'] == password:
                exp_time_stamp = time.mktime(time.strptime(account_data['expire_date'],'%Y-%m-%d'))
                if time.time() > exp_time_stamp:
                    print('\033[31;1mAccount[%s] has expired,please contact the back to get a new card!\033[0m')
                else:
                    return account_data
            else:
                print('\033[31;1mAccount ID or password is incorrect!\033[0m')


def acc_login(user_data,log_obj):
    retry_count = 0
    while user_data['is_authenticated'] is not True and retry_count<3:
        account = input('\033[32;1maccount:\033[0m').strip()
        password = input('\033[32;1mpassword:\033[0m').strip()
        auth = acc_auth(account,password)
        if auth:
            user_data['is_authenticated'] = True
            user_data['account_id'] = account
            return auth
        retry_count += 1
    else:
        log_obj.error('account [%s] too many login attempts'%account)
        exit()