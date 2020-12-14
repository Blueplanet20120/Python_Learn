# 集合、字典的基本運算 - Set、Dictionary
# 集合的运算
s1 = {3, 4, 5}
# print(3 in s1)  # 有无在里面 有就是True
# print(10 not in s1)
s1 = {3, 4, 5}
s2 = {4, 5, 6, 7}
s3 = s1 & s2  # 交集：取两个集合相同的资料
# print(s3)  # {4, 5}
s3 = s1 | s2  # 联集：取两个集合中所以的资料，但不重复放
s3 = s1 - s2  # 差集：从s1中，减去和s2重叠的部分，有顺序性。
s3 = s1 ^ s2  # 反交集：取两个集合中，不重叠的部分
print(s3)
s = set("Hello")  # set(字串）
# print(s)  # {'o', 'e', 'H', 'l'} 自动拆解成集合有什么用？
# 可以判断每个字元是否在里面
# print("H" in s)  # True

# 字典的运算:key-value 配对
dic = {"apple": "苹果", "bug": "虫虫"}
# print(dic)
# print(dic["apple"]) #用key取得value
dic["apple"] = "小苹果"  # 更改内容
# print(dic["apple"])
dic = {"apple": "苹果", "bug": "虫虫"}
print(dic)
del dic["apple"]  # 删除字典中的键值对
print(dic)
# print("apple" in dic) #只对key去判断

# dic={x:x*2 for x in List} #列表的资料当资料去产生字典
dic = {x: x * 2 for x in [3, 4, 5]}
print(dic)
