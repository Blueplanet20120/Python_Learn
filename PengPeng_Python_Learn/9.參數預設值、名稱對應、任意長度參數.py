#參數預設值、名稱對應、任意長度參數
#参数的预设资料
def power(base,exp=0):
    print(base**exp)

#power(3,2) #传出函式3的2次方
#power(20) #exp不写入就是预设值0，任何数字的0次方等于1，因此呼叫函式结果是1
#使用参数名称对应
def divide(n1,n2):
    print(n1/n2)
divide(2,4)
divide(n2=33,n1=12) #通过参数名称对应，不管顺序性，这是python给出的灵活性
#无限/不定参数资料
def avg(*ns):
    sum=0
    for n in ns:
        sum=sum+n
    print(sum/len(ns)) #总和除以列表的长度就是平均数
avg(3,4) #tuple格式的有序列表结果：(3, 4)
avg(5,6,8,90)

