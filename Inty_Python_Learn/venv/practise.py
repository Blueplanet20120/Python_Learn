import requests #安装requests pip install requests
text=requests.get('http://news.baidu.com/?tn=news')
print(text.content)
