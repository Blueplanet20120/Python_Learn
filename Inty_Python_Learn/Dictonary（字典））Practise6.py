'''
Python 3 中有六个标准的数据类型：
Number（数字）
String（字符串）
List（列表）
Tuple（元组）
Sets（集合）
Dictonary（字典）
……

'''
#Dictonary（字典）
myDic = {'key':"value","key2":"value"}
myPhones = {"Ihpne X":1000,"Sumsang":9000}
#print(myPhones)
Iphone_Price = myPhones["Ihpne X"]
print("Iphone price: " +str(Iphone_Price))
#change key values
myPhones["Ihpne X"]=500
print(myPhones)
Iphone_Price2 = myPhones["Ihpne X"]
print("Iphone price: " +str(Iphone_Price2))
#清除数据
myPhones.clear()
print(myPhones)










