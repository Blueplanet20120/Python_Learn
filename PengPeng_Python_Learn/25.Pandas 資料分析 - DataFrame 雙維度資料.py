#Pandas 資料分析 - DataFrame 雙維度資料
import pandas as pd
#以字典资料为底，建立DataFrame
#pd.DataFrame(字典，index=索引列表)
#取得一整列 data.iloc[顺序]
#取得一个整列 data.loc[索引]

#取得栏位（Colum） 相当于exsle里面 A B C

#资料索引
data=pd.DataFrame({
    "name":["Amy","Bob","Charles"],
    "salary":[30000,50000,40000]
},index=["a","b","c"])
print(data)
print("#########################")
#观察资料
# print("资料的数量",data.size)
# print("资料的形状（列、栏）",data.shape)
# print("资料索引",data.index)
#取得列（Row\横向)的Series资料:根据顺序,根据索引
print("取得第二列",data.iloc[1],sep="\n")
print("##################")
print("取得第七列",data.loc["c"],sep="\n")
#取得栏(Colum/直向)的 Series 资料:根据栏位的名称
print("取得 name 栏位",data["name"],sep="\n")
names=data["name"] #取得单维度 Series 资料
print("把 name 全部转大写",names.str.upper(),sep="\n")
salaries=data["salary"]
print("薪水的平均值",salaries.mean(),sep="\n")

#建立新的栏位
print("############################")
data["revenue"]=[50000,60000,40000] #data[新栏位]=列表
#另外一种新增栏位的写法
data["rank"]=pd.Series([3,6,8],index=["a","b","c"]) #data[新栏位的名称]=Series 的资料
data["cp"]=data["salary"] #根据现有栏位复制新的一栏
data["cp"]=data["revenue"]/data["salary"] #通过两个栏位相除,并复制为新栏位"cp"
print(data)

print("############################")











