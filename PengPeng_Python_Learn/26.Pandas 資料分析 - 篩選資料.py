#Pandas 資料分析 - 篩選資料
#载入 pandas 模组
import  pandas as pd
#筛选练习 - Series
data=pd.Series([30,15,20])
#condition=[True,False,True]
condition=data>18 #本质上也是透过布林值来判断
filterData=data[condition]
print(filterData)
print("########################")
data=pd.Series(["您好","Python","Pandas"])
#condition=[False,True,True]
condition=data.str.contains("P") #字串的判断是否包涵 P 再用筛选结果筛选
filterData=data[condition]
print(filterData)

#筛选练习 - DataFrame
print("######### 筛选练习-DataFrame ###############")
data=pd.DataFrame({
    "name":["Amy","Bob","Charles"],
    "salary":[30000,50000,40000]
})
print(data)
print("########################")
#condition=[False,True,True]
#condition=data["salary"]>30000
condition=data["name"]=="Amy"
filterData=data[condition]
print(filterData)


