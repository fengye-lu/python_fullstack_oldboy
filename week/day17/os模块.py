# -*- coding: utf-8 -*-
# @Time    : 2020/2/16 17:02
# @Author  : Jackey-lu
# @File    : os模块.py

import os

# print(os.getcwd())  #  获取当前工作目录路径
# # print(os.chdir('dirname'))  #  改变当前脚本工作目录；相当于shell下的cd
# print(os.curdir)  #返回当前目录
# print(os.pardir)  #  获取当前目录的父目录字符串名
# os.makedirs('a\\b\\c')  #  生成多路径文件夹
# os.removedirs('a\\b\\c') #  若目录为空，则删除，并递归到上一级目录，如也为空，则也删除
# os.mkdir('a.txt')  #  生成单级目录，相当于shell中的mkdir dirname
# os.rmdir('a') # 删除单级目录，且必须是空目录
# dirs = os.listdir(r'G:\fullstack\week\day17')  #展示该目录路径下的全部文件，r就是raw让该字符串是原生字符串
# print(dirs)
# os.remove()  #  删除单个文件，不能删除文件夹
# os.rename('oldname','newname')  # 重命名文件/目录
# info = os.stat('.\\时间模块.py')  # 获得文件/目录的信息
# print(info)  #  获得该文件的信息
# print(info.st_size)  #  获得该文件的大小
# os.sep  # 输出操作系统特定的路径分隔符，win下为"\\" Linux下为"/"
# os.system('bash command')  # 运行shell命令，直接显示
# env = os.environ  # 获取系统环境变量
# print(env)
# abspath = os.path.abspath('os模块.py') # 返回path规范化的绝对路径
# print(abspath)
# s = os.path.split(r"E:\Python3.6.6\python.exe G:/fullstack/week/day17/os模块.py")  # 将path分割成目录和文件名二元组返回
# print(s)
# os.path.dirname(path) # 返回path的目录，其实就是os.path.split(path)的第一个元素
# print(os.path.dirname(r'E:\Python3.6.6\python.exe G:/fullstack/week/day17/os模块.py'))
# os.path.exists(path)  # 判断一个文件是否存在，返回的是布尔值类型
# os.path.isdir()
# os.path.isfile()
# os.path.isabs()
# os.path.join(path1[,path2[,...]]) #将多个路径组合后返回