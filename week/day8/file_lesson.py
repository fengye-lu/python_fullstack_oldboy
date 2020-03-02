# __author:  FENGYE
# data:  2019/12/19

f = open('./jiangjinjiu2.txt', 'r', encoding='utf8')
# print(f.read(17).strip())
print(f.readline().strip())
print(f.readline().strip())
# print(f.readlines())

# number = 0
# for index, i in enumerate(f.readlines()):
#     if index == 1:
#         i = ''.join([i.strip(),'长恨歌'])
#     print(i.strip())

# for i in f :  #for 内部将f对象做成一个迭代器，用一个取一个
#     print(i.strip())

print(f.tell())
# print(f.read(5))   # 每个中文字符占三个字节
# print(f.tell())
# f.seek(0)
# print(f.read(5))

import sys, time

# for i in range(30):
#      sys.stdout.write('*') #sys.stdout是终端操作
#      sys.stdout.flush()  # 不先进入缓冲区，直接进入磁盘
#      time.sleep(0.2)

# for i in range(30):
#     print('*',end='',flush=True)
#     # sys.stdout.flush()  # 不先进入缓冲区，直接进入磁盘
#     time.sleep(0.2)

# f = open('./jiangjinjiu2.txt','a',encoding='utf8')
# f.truncate(20)

# f = open('./jiangjinjiu2.txt','r+',encoding='utf8')
# print(f.readline())
# f.write(' 长恨歌')

# f = open('./jiangjinjiu2.txt','w+',encoding='utf8')
# print(f.readline())
# f.write('李白')
# print(f.tell())
# f.seek(0)
# print(f.readline())

# f = open('./jiangjinjiu2.txt','r',encoding='utf8')
# v_write_ = open('./copy.txt', 'w', encoding='utf8')
# number = 0
# for i in f:
#     number += 1
#     if number == 2:
#         i = ''.join([i.strip(),'李白\n'])
#     v_write_.write(i)
# v_write_.close()
# f.close()



