def print_info(name, age, sex='male'):
    print('Name: %s'%name)
    print('Age: %s'%age)
    print('Sex: %s'%sex)


print_info(age=23,name='fengye')
print_info(age=18,name='luzhenghao')
print_info(age=24,name='yixiaoqing',sex='female')

# function(name,sex='female',*args,**fargs) 参数的固定顺序

