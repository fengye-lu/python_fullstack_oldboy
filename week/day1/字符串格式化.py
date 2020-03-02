# __author:  FENGYE
#  data:  2019/12/10

name = input("Name:")
age = int(input("Age:"))
job = input("Job:")
salary = input("Salary:")

if salary.isdigit():
    salary = int(salary)
else:
    exit("must input digit!")


print(name,age,job,salary)

msg = '''
--------INFO OF %s---------
Name : %s
Age : %d
Job : %s
Salary : %d
You will be retired in %d
-----------end---------------
''' % (name,name,age,job,salary,65-age)

print(msg)
