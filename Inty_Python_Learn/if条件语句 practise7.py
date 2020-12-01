#if statement.py if语句
a=10
b=50
#python 语言从头部写 空行是有格式的
if b > a:
    print('hello')

#if elif else
# age = input("please enter your age: ")
# print(type(age))
# #测试什么数据类型 目前是str类型 想变成数字类型 这要加int()：
age = int(input("please enter your age: "))
#print(type(age))

if age<21:
    print("you can not smoke ")
elif age==21:
    print("you are now 21, you can smoke")
elif age==100: #对于=是赋值，==是等于的意思。
    print("you are 100 years old,please quit smoking")
else:
    print("you can smoke")
