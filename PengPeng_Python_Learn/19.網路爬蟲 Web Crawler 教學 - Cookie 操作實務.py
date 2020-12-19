# 網路爬蟲 Web Crawler 教學 - Cookie 操作實務
# 抓取 PTT 八卦版的网页原始码（HTML)
def getData(url):
    import urllib.request as req
    # 建立一个 Request 物件，附加 Request Headers的资讯
    request = req.Request(url, headers={
        "cookie": "over18=1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"

    })
    with req.urlopen(request) as response:
        data = response.read().decode("utf-8")
    # print(data)

    # 解析原始码，取得每篇文章的标题
    import bs4  # beautifulsoup4调用套件

    root = bs4.BeautifulSoup(data, "html.parser")  # 让 beautifulsoup4 协助我们解析HTML
    print(root.title.string)  # 抓到标签里面的文字
    # find 找到符合条件的一个标签，find_all找到所有
    titles = root.find_all("div", class_="title")  # 寻找class=“title"的 div 标签
    for title in titles:
        if title.a != None:  # 如果标题包含标签（没有被删除）.印出来
            print(title.a.string)
    # 抓取下一页的链接
    nextLink = root.find("a", string="‹ 上頁")  # 找到内文是 ‹ 上頁 的 a 标签
    # print(nextLink)
    return nextLink["href"]  # 抓到元素href内容


pageURL = "https://www.ptt.cc/bbs/Gossiping/index.html"
conut = 0
while conut < 5:  # 回圈自动抓取5页的资料
    pageURL = "https://www.ptt.cc/" + getData(pageURL)
    conut += 1
