# 有序列表的基本運算 - List、Tuple
# 有序列表的基本運算 List
# grades=[12,60,15,70,90]
# print(grades)
# print(grades[0]) #取得列表中的资料
# grades[0]=55 #把55放到第一个位置
# print(grades)
grades = [12, 60, 15, 70, 90]
grades=grades+[12,33] #列表的串接
#print(grades[1:4])  # 同样不包含4本身
#rades[1:4] = []  # 连续删除列表中从编号1到编号4（不包括）的资料
print(grades)
#[12, 60, 15, 70, 90, 12, 33]
print(len(grades)) #取得列表从长度
#7


#巢状列表-组合列表
data=[[3,4,5],[6,7,8]]
#print(data[0][1]) #【0】代表第一列表【1】代表第一个列表的第二个数字
data[0][0:2]=[5,5,5] #代表从第一个列表中替换掉1-2个数字的内容换成后边的[5,5,5]
#print(data)

# 有序列表的基本運算 Tuple
data=(3,4,5)
#data[0]=5 #错误：Tuple 的资料不可以更改
print(data[2])
#Tuple的操作都和List一样 唯一不同的是Tuple的资料不能变动