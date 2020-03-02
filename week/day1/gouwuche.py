# __author:  FENGYE
# data:  2019/12/12


print('----------欢迎来到fengye商城---------')
count = 0
goods = {'iphone':5644,'mac book':9000,'coffee':32,'python book':80,'bicycle':1500}
salary = input('您的预算:')
if salary.isdigit():
    salary = int(salary)
    while salary > 0 :
        want_goods = input('您想购买的物品：')
        for index,i in enumerate(goods,1):
            if want_goods == i:
                salary = salary - goods[i]
                print("您的余额为：",salary,"您选的商品编号为：",index)
                count += 1
        if count > 0:
            count = 0
            continue
        if want_goods == 'exit':
            print("-----欢迎下次光临，再见！------")
            break
        else:
            print("您输入的商品有误！")
    if salary <= 0:
        print("对不起您的余额不足！")
else:
    print("please input right number!")
