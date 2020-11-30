#while loop practise9
#while loop 需要条件的循环语句
condition=1
while condition<10:
    print(condition)
    condition=condition+1 #每循环一次＋1，直到conditon>=10停止
#    break #停下来的意思

#示例2
while  True:
    a=int(input("please enter number a: "))
    b=int(input("please enter number b: "))
    c=int(input("please enter number c: "))

    print("您运算的结果是：" +str(a+b+c))
    break