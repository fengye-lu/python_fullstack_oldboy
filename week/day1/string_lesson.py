# __author:  FENGYE
# data:  2019/12/13

st = 'hello kitty {name} is {age} '

print(st.count('l'))          # 统计元素个数
print(st.capitalize())        # 首字母大写
print(st.center(50,'#'))      #居中并且用设置的符号填
print(st.endswith('tty'))     #判断是否以某个内容结尾
print(st.startswith('he'))    #判断是否以某个内容开头
print(st.find('t'))           #查找第一个元素，并将索引值返回
print(st.format(name='fengye',age='22'))  #格式化输出的另一种方式
print(st.format_map({'name':'fengye','age':22}))
print(st.index('i'))
print('asa'.isalnum())
print('1231232'.isdigit())    #判断是不是一个数字并且为整数
print('sa'.islower())
print('DS'.isupper())         #判断字符是否为大小写
print(' '.isspace())          #判断是否为空格
print('My Title'.istitle())   #判断是否是标题
print('My Space'.lower())     #将字符的大写变成小写
print('My Space'.upper())     #将字符的小写变成大写
print('My Space'.swapcase())  #将字符的大写变成小写，小写变成大写
print('     My space\n'.strip())#去掉字符中存在空格和换行符
print('My title title'.replace('title','body',1)) #替换字符中的内容,1表示替换几个
print('My title title'.split(' '))   #把字符串通过一定的字符划分成列表

