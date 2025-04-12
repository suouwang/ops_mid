import requests as rq
from bs4 import BeautifulSoup
import json

headers = {
    'User-Agent': 'Mozilla/5.0 (compatible; GitHubActionsBot/1.0)'
}

def readurl(url, jFile, count):
    if count == 3:
        return
    response = rq.get(url,headers=headers)
    soup = BeautifulSoup(response.text, "lxml")
    for inf in soup.find_all("div", class_="title"):
        a = inf.find('a')
        if a and not a.text.startswith('[公告]'):
            json_ori = {'title': a.text, 'url': 'https://www.ptt.cc' + a['href']}
            json.dump(json_ori, jFile, indent=2, ensure_ascii=False)
            jFile.write(',\n')  # 如果你打算存成一個 array，也可改用 list

    for btn in soup.find_all('a', class_="btn wide"):
        if btn.text == '‹ 上頁':
            readurl('https://www.ptt.cc' + btn['href'], jFile, count + 1)

if __name__ == "__main__":
    with open('file.json', 'w', encoding="utf-8") as jFile:
        readurl("https://www.ptt.cc/bbs/HardwareSale/index.html", jFile, 0)
