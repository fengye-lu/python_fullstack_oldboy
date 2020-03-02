#__author:  FENGYE
#data:  2019/12/11

# passed_authentication = False
# for i in range(5):
#     _user = "fengye"
#     _password = "123456"
#
#     username = input("username:")
#     password = input("password:")
#
#     if username == _user and password == _password:
#         print("login success")
#         passed_authentication = True
#         break
#     else:
#         print("please login again in right way")
#         continue
#
# if not passed_authentication:
#     print("it's enough ,please stop input")
#
#
# for epoch in range(1,100,2): # 2代表的是步长
#     print(epoch)

for i in range(5):
    _user = "fengye"
    _password = "123456"

    username = input("username:")
    password = input("password:")

    if username == _user and password == _password:
        print("login success")
        break
    else:
        print("please login again in right way")
        continue

else:  # 只要上面的for循环没有被正常的打断就执行这个else
    print("it's enough ,please stop input")