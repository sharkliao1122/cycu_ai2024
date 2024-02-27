import feedparser
import requests

# 設定 RSS feed 網址
url = 'https://feeds.feedburner.com/rsscna/politics'

# 使用 feedparser 解析 RSS feed
feed = feedparser.parse(url)

# 迴圈遍歷每一個 feed entry
for entry in feed.entries:
    # 取得標題
    title = entry.title

    # 使用 requests 取得該標題的網頁內容
    response = requests.get(entry.link)

    # 列印標題和回傳的網頁內容
    print(f'Title: {title}')
    print(f'Content: {response.text}')
    #列印summarize
    print(f'Summary: {entry.summary}')
    print('-----------------------------------')

#若是標題中含有台灣，則列印出來，並用紅色字體標示

    if '台灣' in title:
        print('\033[31m' + title + '\033[0m')   #紅色字體   