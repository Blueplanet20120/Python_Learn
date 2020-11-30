#-funciton函数
#define 下定义
# def func1_name():
#     print("hello funciton")
#
#
#
# func1_name()

a=10
b=10
print(a+b)

c=20
d=20

print(c+d)

#比较麻烦 函数就简单了

def sum(a,b):
    print(a+b)


sum(2,3) #利用函数自定义代值，非常方便计算

def fun2():
    return "hello fun2" #这是赋值，方便调用，不打印

a=fun2()

print(a)


#复习一下之前的内容
def coverter(weight):
    ponds=weight/0.45 #公斤换算成磅
    print(ponds)

coverter(60) #60公斤等于133.333磅

def coverter2(weight=100): #有默认值，需要更改就要coverter2(weight=300)
    ponds=weight/0.45 #公斤换算成磅
    print(ponds)

#直接调用或者可以赋值调用
coverter2()





