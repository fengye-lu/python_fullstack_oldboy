def comput(*args):
    z = float(args[0][0])
    for index, s in enumerate(args[0]):
        if s.isnumeric():
            pass
        elif s == '+':
            z = z+float(args[0][index+1])
        elif s == '-':
            z = z-float(args[0][index+1])
        elif s == '*':
            z = z*float(args[0][index+1])
        elif s == '/':
            z = z/float(args[0][index+1])
        else:
            print("请输入正确的字符！")
    return z


num1 = input('请输入：')
print('您的答案是%s'%comput(num1))