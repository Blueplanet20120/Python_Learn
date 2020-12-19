#網路爬蟲 Web Crawler 教學 - AJAX XHR 網站技術分析實務
#AJAX / XHR两个是一个技术两种叫法，在浏览器里network里选择XHR作为分析
#抓取 Medium.com 的文章
import urllib.request as req

url = "https://medium.com/_/api/home-feed"
# 建立一个 Request 物件，附加 Request Headers的资讯
request = req.Request(url, headers={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"

})
with req.urlopen(request) as response:
    data = response.read().decode("utf-8")
#print(data)

# 解析原始码 json格式，取得每篇文章的标题
import json
data = data.replace("])}while(1);</x>","") #把网页开头不符合json格式的乱码”])}while(1);</x>“ 替换为空值
data = json.loads(data) #把原始的 JSON 资料解析成字典、列表的表现形式
#取得 JSON 资料中的文章标题
posts = data["payload"]["references"]["Post"]
for key in posts:
    post=posts[key]
    print(post["title"])

