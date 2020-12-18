# 網路連線程式、公開資料串接
# 网路连线
# import urllib.request as request
# src="https://www.ntu.edu.tw/"
# with request.urlopen(src) as response:
#     #data=response.read() #取得台湾大学网站的原始码 （HTML\CSS\JS)
#     data = response.read().decode("utf-8") #想显示中文后面加.decode(“utf-8")
# print(data)


# 串接、截取公开资料
import urllib.request as request
import json

src = "https://data.taipei/api/v1/dataset/a861044a-8683-4ccd-b34e-c606c23c2d47?scope=resourceAquire"
with request.urlopen(src) as response:
    data = json.load(response)  # 用json模組讀取資料，会处理好一些细节
# print(data)

# 将公司名称列表出来
clist = data["result"]["results"]
print(clist)  # 已经是列表的方式[]印出来
# 打開檔案的方式,以回圈形式讀取資料,寫入檔案
with open("data.txt", "w", encoding="utf-8") as  file:
    for company in clist:
        file.write(company["終止營業日期"] + "\n")  # 以字典的方式列出key,取得value 并寫入檔案data.txt
