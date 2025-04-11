import requests as rq
from bs4 import BeautifulSoup
import json

url = "https://www.ptt.cc/bbs/HardwareSale/index.html"
response = rq.get(url)
soup = BeautifulSoup(response.text,"lxml")
#print(soup.prettify())

def readurl(url,f,f2,jFile,count):
    if count == 3:
        return None
    response = rq.get(url)
    soup = BeautifulSoup(response.text,"lxml")
    #print(soup.prettify())
    f2.write(soup.prettify())
    for inf in soup.find_all("div",class_="title"):
        a = inf.find('a')
        if a != None:
            r = a.text
            if not(r.startswith('[公告]')):
                json_ori = {'title':r,
                            'url':'https://www.ptt.cc'+a['href']}
                json.dump(json_ori,jFile,indent=2,ensure_ascii=False)
                f.write(a.text+'\n')
                f.write('https://www.ptt.cc'+a['href']+'\n\n')
    ##
    for btn in soup.find_all('a',class_="btn wide"):
        if btn.text == '‹ 上頁':
            readurl('https://www.ptt.cc'+btn['href'],f,f2,jFile,count+1)



f2 = open('html.txt','w', encoding='utf-8')
f = open('text.txt','w', encoding='utf-8')
jFile = open('file.json','w',encoding="utf-8")
count = 0
readurl(url,f,f2,jFile,count)