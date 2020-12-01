#list comprehension
newList=[]
for i in range(11):
    newList.append(i*2)
print(newList)

#下面是简洁模式表达方式
print([i*2 for i in range(11)])

list=['小明','王二','王八','李四']
emptylist=[]
for name in list:
    if name.startswith('王'): #startswith-从里面挑选出王姓的
        emptylist.append(name) #append() 转换成列表

print(emptylist)

