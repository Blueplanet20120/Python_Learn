#迴圈進階控制，break、continue、else 命令
#break的简易范例
n=0
while n<5:
    if n==3:
        break
    print(n) #印出回圈的 n

    n+=1
print("最后的n: ",n)

#continue
n=0
for x in [0,1,2,3,]:
    if x%2==0: #x 是偶数
        continue
    print(x)
    n+=1
print("最后的n： ",n)