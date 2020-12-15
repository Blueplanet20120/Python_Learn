# 函式基礎：定義並呼叫函式
# 函式的定义：程式码包装在一个区块中，方便随时呼叫使用
# 先定义函式-才能呼叫函式，有两个步骤
#
# 定义函式 没有被呼叫是不会被执行的
def multiply(x, y):
    print(x * y)


# 呼叫函式

multiply(5, 6)
multiply(10, 33)
value = multiply(3, 4)
print(value)  # 结果是none 因为没return 默认是none


def multiply(x, y):
    # print(x*y)
    return x * y


value = multiply(3, 4)
print(value)


# 回传return 可以把结果带出来继续用

# 程式的包装 同样的逻辑可以重复利用
def calculate(max):
    sum = 0
    for n in range(1, max):
        sum = sum + n
    print(sum)


calculate(90)  # 函式的呼叫 记住没呼叫就不会执行。
calculate(20)
