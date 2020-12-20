#文字檔案的讀取和儲存
#流程：开启档案-读取档案-关闭档案
#档案物件=open（档案路径,mode=开启模式）
# file=open("data.txt",mode="w",encoding="utf-8") #开启 编码开启中文能正常处理
# file.write("Hello File Yang Yang\nSecond Line\nThrid Line\n测试中文") #操作
# file.close() #关闭
# #比较好的程式 with as 不需要close，会自动关闭档案
 with open("data2.txt",mode="w",encoding="utf-8") as file:
     file.write("3\n4\n5\n6")
#
# #档案的读取
# with open("data.txt",mode="r",encoding="utf-8") as file:
#     data=file.read()
# print(data)
#想一行一行的读取，加入总和，特别适合数字类别的档案处理
sum=0
with open("data2.txt",mode="r",encoding="utf-8") as file:
    for line in file:
        sum+=int(line)
print(sum)

#使用 json 格式读取、写入档案
import json
with open("config.json",mode="r") as file:
    data=json.load(file) #读取json的资料 是一个字典
print("name",data["name"]) #用读取字典的方式 读取key 得到value
print(data) #字典形式
data["name"]="New Nanme" #修改变数中的资料
#把最新的资料更新回档案中 复写
with open("config.json",mode="w") as file:
    json.dump(data,file) #修改变数资料后，最终复写回档案
print(data)

