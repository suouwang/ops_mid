import requests as rq
from bs4 import BeautifulSoup
import json

url = "https://www.ptt.cc/bbs/HardwareSale/index.html"
response = rq.get(url)
soup = BeautifulSoup(response.text,"lxml")
#print(soup.prettify())

def readurl(url,jFile,count):
    print("Count: "+str(count+1))
    if count == 3:
        return None
    response = rq.get(url)
    soup = BeautifulSoup(response.text,"lxml")
    print(soup.prettify())
    for inf in soup.find_all("div",class_="title"):
        a = inf.find('a')
        if a != None:
            r = a.text
            if not(r.startswith('[公告]')):
                json_ori = {'title':r,
                            'url':'https://www.ptt.cc'+a['href']}
                print(json_ori)
                json.dump(json_ori,jFile,indent=2,ensure_ascii=False)
    ##
    for btn in soup.find_all('a',class_="btn wide"):
        if btn.text == '‹ 上頁':
            readurl('https://www.ptt.cc'+btn['href'],jFile,count+1)

with open('file.json', 'w', encoding="utf-8") as jFile:
        readurl("https://www.ptt.cc/bbs/HardwareSale/index.html", jFile, 0)
