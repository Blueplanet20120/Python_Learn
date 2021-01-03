#迴圈基礎，while 迴圈、for 迴圈
#使用range(）可以快速生成一个列表
# range(5)
print(range(5))
for i in range(5):
    print(i)
# # while回圈
n=1
sum=0
# while n<=10:
#     sum=sum+n
#     n+=1
# print(sum)

#for回圈
# for x in "Hello":
#     print(x)
# for x in range(5,10):
#     print(x)
sum=0
for x in range(1,11):
    sum=sum+x
print(sum)