# -*- coding: utf-8 -*-
# @Time    : 2020/2/19 12:20
# @Author  : Jackey-lu
# @File    : 配置文件模块.py

import configparser

config = configparser.ConfigParser()

# config['DEFAULT'] = {'ServerAliveInterval':'45',
#                      'Compression':'yes',
#                      'CompressionLevel':'9'}
#
# config['bitbucket.org'] = {}
# config['bitbucket.org']['User'] = 'hg'
# config['topsecret.server.com'] = {}
# topsecret = config['topsecret.server.com']
# topsecret['Host Port'] = '50022'
# topsecret['ForwardX11'] = 'no'
# config['DEFAULT']['ForwardX11'] = 'yes'
#
# with open('example.ini', 'w') as configfile:
#     config.write(configfile)

config.read('example.ini')
print(config.sections())
print(config.defaults())