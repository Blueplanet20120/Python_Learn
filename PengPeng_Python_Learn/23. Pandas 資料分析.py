# Pandas 資料分析
# 概念类似试算表的资料分析套件
# 步骤:
# 1.安装 Pandas 套件 pip install pandas
# 2.认识单维度的资料 Series
# 3.认识双维度的资料 DataFrame
###
# 载入 pandas 模组
import pandas as pd

# 建立单维度的资料 Series
data = pd.Series([20, 10, 15])
print(data)
# 基本 Series
print(data.max())
print(data.median())
data=data*2 #全部扩大两倍
print(data)
data=data==20 #比较data里是否与20相等，用布林值标注出来
print(data)

# 建立双维度的资料 DataFrame
data=pd.DataFrame({
    "name":["Amy","John","Bob","Perfume"],
    "salary":[30000,50000,40000,60000]
})
# 基本DataFrame操作
#print(data)
#取得特别的栏数
print(data["name"])
#取得特定的列
print(data.iloc[1]) #印出第二列










