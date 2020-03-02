# -*- coding: utf-8 -*-
# @Time    : 2020/2/19 13:05
# @Author  : Jackey-lu
# @File    : 正则表达式.py

import re

# ret = re.findall('w\w{2}l','hello world')
# print(ret)

# ret =re.findall('lzh','dsfsfsflzhfsfsffs')
# print(ret)


# 元字符

# .通配符
# ret = re.findall('w..l','hello world')  # .只能代指任意一个字符
# print(ret)

# ^
# ret = re.findall('^h...o','hlsaodfhello')
# print(ret)

# $
# ret = re.findall('a..x$','ffafsfsfsalexfsfs')
# print(ret)

# *:重复匹配[0,+oo)
# ret = re.findall('a*','fsfsfafdfs')
# print(ret)

# +:[1,+oo)
# ret = re.findall('as+','fsafsfafsfa')
# print(ret)

# ret = re.findall('a+f','fsafsfafsfa')
# print(ret)

# ? [0,1]
# ret = re.findall('a?b','aaaabhghabfb')
# print(ret)

# {}
# ret =re.findall('a{5}b','aaaaab')
# print(ret)

# ret =re.findall('a{1,5}b','dsdaab')
# print(ret)

# 结论： *等于{0,+oo}, +等于{1,+oo}, ？等于{0,1}


# 字符集
# ret = re.findall('a[cde]x','aex')
# print(ret)

# ret = re.findall('[a-z]','aex')
# print(ret)

# ret = re.findall('[1-9a-zA-Z]','aexsfs3feff34ff')
# print(ret)

# ^放在[]里表示取反
# ret = re.findall('[^t]','ijishiftst')
# print(ret)

# ret = re.findall('[^ts]','ijishiftst')
# print(ret)

# \
# 反斜杠后边跟元字符去除特殊功能。
# 反斜杠后边跟普通字符实现特殊功能。
# \d 匹配任何十进制数；他相当于类[0-9]。
# \D 匹配任何非数字字符；他相当于类[^0-9].
# \s 匹配任何空白字符；它相当于类[\t\n\r\f\v]。
# \S 匹配任何非空白字符；它相当于类[^\t\n\r\f\v]。
# \w 匹配任何字母数字字符；它相当于类[a-zA-Z0-9_]。
# \W 匹配任何非字母数字字符；它相当于类[^a-zA-Z0-9_]
# \b: 匹配一个特殊边界

# print(re.findall('\d{11}','fsfsfs124424232342432dsd324'))
# print(re.findall('\sasd','sff asd'))
# print(re.findall(r'I\b','hello, I am a LIST'))

#######################################

#() |
# print(re.search('(as)+','sdsfsfsfasas').group())
# print(re.search('(as)|3','as3').group())


#正则表达式的方法

# 1  findall(): 所有结果都返回到一个列表中
# 2  search(): 返回匹配到的第一个对象（object），对象可以调用group（）返回结果
# 3  match()： 只在字符串开始匹配,也回匹配到的第一个对象（object），对象可以调用group（）返回结果

# ret = re.match('ddf','ddffsfsddf')
# print(ret.group())

# 4  split()
# ret = re.split('k','fsfskfsf')
# print(ret)
# ret = re.split('[fg]','dsdfskigls')
# print(ret)

# 5  sub()
# ret = re.sub('a..x','s..b','sfdalexfsfs')
# print(ret)

# 6 compile()
# ret1 = re.findall('\.com','dadafdfs.comadda')
# print(ret1)
# obj = re.compile('\.com')
# ret2 = obj.findall('dadafdfs.comadda')
# print(ret2)