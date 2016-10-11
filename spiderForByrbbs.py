# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
import alfred

homeUrl = "http://bbs.cloud.icybee.cn/default"
titleArray = []
linkArray = []
itemArray = []

def fetchLinkAndTitle(url):
    html = requests.get(url).text
    soup = BeautifulSoup(html,"html.parser")
    for ul in soup.find_all('ul'):
        if ul.get('id') == 'column2':
            for title in ul.find_all('li')[1:11]:
                titleArray.append(title.get('title'))
            for link in ul.find_all('a')[1:11]:
                linkArray.append("http://bbs.byr.cn/#!" + link.get('href')[1:])

def makeXML():
    for i in range(10):
        item = alfred.Item(uid='hex',arg=linkArray[i],title=titleArray[i],subtitle="",icon="icon.png")
        itemArray.append(item)
    print alfred.render(itemArray)

def main():
    fetchLinkAndTitle(homeUrl)
    makeXML()

if __name__ == '__main__':
    main()



