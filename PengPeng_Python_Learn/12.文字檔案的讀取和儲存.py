#文字檔案的讀取和儲存
#流程：开启档案-读取档案-关闭档案
#档案物件=open（档案路径,mode=开启模式）
file=open("data.txt",mode="w",encoding="utf-8") #开启 编码开启中文能正常处理
file.write("Hello File Yang Yang\nSecond Line\nThrid Line\n测试中文") #操作
file.close() #关闭
#比较好的程式 with as 不需要close，会自动关闭档案
with open("data2.txt",mode="w",encoding="utf-8") as file:
    file.write("3\n4\n5\n6")

#档案的读取
with open("data.txt",mode="r",encoding="utf-8") as file:
    data=file.read()
print(data)
#想一行一行的读取，加入总和，特别适合数字类别的档案处理
sum=0
with open("data2.txt",mode="r",encoding="utf-8") as file:
    for line in file:
        sum+=int(line)
print(sum)

#使用 json 格式读取、写入档案
