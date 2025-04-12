from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
import csv

driver = webdriver.Edge()
driver.implicitly_wait(2)
driver.get("https://www.coolpc.com.tw/evaluate.php")
action = ActionChains(driver)
time.sleep(0.1)
action.move_by_offset(50, 50).click().perform()
f = open('app.csv','w', newline = '',encoding='utf-8-sig')
writer = csv.writer(f)

def collector(driver,name,writer):
    a = driver.find_element(By.NAME,name)
    #print(a.text)
    for r in a.text.split('\n'):
        #if r.startswith('共有商品'):
        #    continue
        a = r.split(', ')
        if len(a) == 2:
            writer.writerow([a[0],a[1]])

a = ['4','5','6','12']

for i in a:
    collector(driver,'n'+i,writer)