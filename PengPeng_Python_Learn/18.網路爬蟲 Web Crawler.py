#網路爬蟲 Web Crawler
#HTML解析第三方套件pip install beautifulsoup4

#抓取 PTT 电影版的网页原始码（HTML)
import  urllib.request as req
url="https://www.ptt.cc/bbs/movie/index.html"
#建立一个 Request 物件，附加 Request Headers的资讯
request=req.Request(url,headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"

})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")
#print(data)

# 解析原始码，取得每篇文章的标题
import bs4 #beautifulsoup4调用套件
root=bs4.BeautifulSoup(data,"html.parser") #让 beautifulsoup4 协助我们解析HTML
print(root.title.string) #抓到标签里面的文字
#find 找到符合条件的一个标签，find_all找到所有
titles=root.find_all("div",class_="title") #寻找class=“title"的 div 标签
for title in titles:
    if title.a != None: #如果标题包含标签（没有被删除）.印出来
        print(title.a.string)



