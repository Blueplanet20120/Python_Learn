#Flask 網站開發 - 基礎環境建置教學
#主要的步骤:
###
# 1 安装 Flask 套件 pip install flask
# 2 建立专案资料夹\","撰写程式
# 3 启动伺服器\","测试网站运作
###建立简单的网站伺服器代码
from flask import Flask
app=Flask(__name__) #__name__ 代表目前执行的模组
@app.route("/") # @ 函式的装饰(Decorator):以函式为基础,提供附加的功能
def home():
    return "Hello flask"
@app.route("/test") #代表我要处理网站路径
def test():
    return "This is Test"

if __name__=="__main__": #如果以主程序执行
    app.run() #立刻启动伺服器

