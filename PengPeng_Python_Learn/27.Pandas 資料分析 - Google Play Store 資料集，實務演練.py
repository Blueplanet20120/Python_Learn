# Pandas 資料分析 - Google Play Store 資料集，實務演練
# 收集资料: https://bit.Iy/2UMcbDI
import pandas as pd

# 读取资料
data = pd.read_csv("googleplaystore.csv")  # 把 csv 格式的档案读取成一个DataFreame
# 观察资料
print("资料的数量", data.shape)
print("资料的栏位", data.columns)
print("#####################")
# 分析资料:评分的各种统计数据
# condition=data["Rating"]<=5 #排除大于5 评分的资料
# data=data[condition]
# print(data)
# print(data["Rating"]) #查看所有应用程式的评分
# print("平均数",data["Rating"].mean())
# print("中位数",data["Rating"].median())
# print("取得前一千个应用程式的平均",data["Rating"].nlargest(1000).mean())
# 分析资料:安装数量的各种统计数据
# print("############################################")
# print(data["Installs"][10472]) #提示无法处理的资料,可以用这种方法查看,然后再次替换掉了
# data["Installs"]=pd.to_numeric(data["Installs"].str.replace("[,+Free]","").replace("Free",""))
# print("安装栏目的平均数",data["Installs"].mean())
# condition=data["Installs"]>100000
# data=data[condition]
# print("安装数量大于100000的应用有",data.shape[0])

# 基于资料的应用:关键字搜寻应用程式名称
keyword=input("请输入关键字:")
condition=data["App"].str.contains(keyword,case=False)#应用程式栏目 是否包含使用者输入关键字(case=False 忽略大小写)的
print("包含关键字的应用程式的数量",data[condition].shape[0]) #把数量印出来 shape可以统计多少列和栏 0列 1栏
