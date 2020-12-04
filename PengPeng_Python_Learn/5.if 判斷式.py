# if 判斷式
# 判断式
# if True:
#     print("True 执行")
# else:
#     print("上方没执行")

# x=input("请输入数字： ") #取得字串形式的使用者输入讯息
# x=int(x) #将字串形态转变为数字形态
# if   x>200:
#     print("大于200")
# elif x>100:
#     print("大于100，小于等于200")
# else:
#     print("小于等于100")

# 四则运算
n1 = int(input("请输入数字一： "))
n2 = int(input("请使用者输入数字二： "))
# print(n1+n2)
op = input("请输入运算:（+,-,*,/）\n")
print("*************************")
if op == "+":
    print("运算结果=", n1 + n2)
elif op == "-":
    print("运算结果=", n1 - n2)
elif op == "*":
    print("运算结果=", n1 * n2)
elif op == "/":
    print("运算结果=", n1 / n2)
else:
    print("您的输入有误，请重新输入!")
print("*************************")

# 练习时候自己写出来不要看老师的讲解，这样练习更有用
