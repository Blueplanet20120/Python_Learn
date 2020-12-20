#Pandas 資料分析 - Series 單維度資料
#载入 Pandas 模组
import pandas as pd
# #以列表资料为底，建立 Series
# pd.Series(资料列表)
#资料索引
data=pd.Series([5,4,-2,3,7],index=["a","b","c","d","e"]) #自己定义的资料索引
#print(data)
#观察资料
print("资料的形态",data.dtype)
print("资料的数量",data.size)
print("资料的索引",data.index)
#取得资料:根据顺序/根据索引
print(data[2]) #按照顺序取得第三笔资料
print(data["b"],data["d"]) #按照索引取得资料
#数字运算:基本\统计\顺序
print("最大值",data.max())
print("总和",data.sum())
print("标准差",data.std())
print("中位数",data.median())
print("最大的三位数\n",data.nlargest(3))
data=pd.Series(["你好","Python","Pandas"])
#字串运算:基本/串接/搜寻/取代
#print(data.str.lower()) #全部变小写
print("###################")
print(data.str.len()) #算出每个字串的长度
print(data.str.cat(sep="-")) #用"-"串接起来
print(data.str.contains("P")) #判断每个字串是否包涵大写的 P 布林值表现出来
print(data.str.replace("你好","Hello")) #取代操作