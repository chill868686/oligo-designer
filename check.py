import wget

with open('assembly_summary_refseq.txt','r') as f:
    lines = f.readlines()
with open('swzj_c1.txt','r') as f:
    names = [line.strip() for line in f.readlines()]

organism = []    
for name in names:
    a = name
    if name.endswith('virus'):
        a = name[:-6]
    organism.append(a)
for i,o in enumerate(organism):
    for line in lines[1:]:
        if o.upper() in line.split('\t')[7].upper():
            if line.split('\t')[11]=='Complete Genome':
                print(i+1,o)
                url = line.split('\t')[19]
                downloadurl = url+'/'+url.split('/')[-1]+'_genomic.fna.gz'
                print(downloadurl)
                #wget.download(downloadurl,'genome')
                break
'''
import time
import os
import csv
import json
import sys
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import FirefoxOptions
from selenium.webdriver.common.keys import Keys
import openpyxl
import requests

ind = int(sys.argv[1])
ntoc = ["一","二","三","四","五","六","七","八","九"]
ntoe = ["one","two","three","four","five","six","eleven","eight","nine"]

def download_videofile(video_link,file_name):
    root='media/'
    print("文件下载:%s" % file_name)
    r = requests.get(video_link, stream=True).iter_content(chunk_size=1024 * 1024)
    with open(root+file_name, 'wb') as f:
        for chunk in r:
            if chunk:
                f.write(chunk)
    print("%s 下载完成!\n" % file_name)
    
def scroll_shim(passed_in_driver, object):
    x = object.location['x']
    y = object.location['y']
    scroll_by_coord = 'window.scrollTo(%s,%s);' % (
        x,
        y
    )
    scroll_nav_out_of_way = 'window.scrollBy(0, -120);'
    passed_in_driver.execute_script(scroll_by_coord)
    passed_in_driver.execute_script(scroll_nav_out_of_way)


opts = FirefoxOptions()
#opts.add_argument("-headless")
opts.add_argument('--no-sandbox')
driver = webdriver.Firefox(executable_path='./geckodriver', options=opts)

actions = ActionChains(driver)
#driver.maximize_window()

with open('aabb.csv','r') as f:
    hascrawled = [line.split(',')[0] for line in f.readlines()]


driver.get("https://www.douyin.com/")
time.sleep(5)
if True:
    with open('dy_cookies.txt', 'r', encoding='utf8') as f:
        listCookies = json.loads(f.read())
        print(listCookies)
    for cookie in listCookies:
        cookie_dict = {
            'domain': '.douyin.com',
            'name': cookie.get('name'),
            'value': cookie.get('value'),
            "expires": '',
            'path': '/',
            'httpOnly': False,
            'sameSite': 'None',
            'Secure': cookie.get('secure')
        }
        driver.add_cookie(cookie_dict)
    driver.refresh()
actions.send_keys(Keys.DOWN).pause(1).send_keys(Keys.DOWN).perform()

#input("waitforlogin:")
dictCookies = driver.get_cookies()  # 获取list的cookies
jsonCookies = json.dumps(dictCookies)  # 转换成字符串保存
if True:
    with open('dy_cookies.txt', 'w') as f:
        f.write(jsonCookies)
        print('cookies保存成功！')
driver.get("https://www.douyin.com/search/第"+ntoc[ind]+"批在韩国烈士志愿军")
input("waitforlogin:")
time.sleep(5)
index = 0
Data = []
while True:
    if len(Data)>=15:
        break
    lists = driver.find_elements(By.XPATH,"//li[contains(@class,'aCTzxbOJ')][contains(@class,'mZ4vbHBN')]")
    for _ in range(len(lists)-index):
        l = lists[index]
        scroll_shim(driver, l)
        time.sleep(10)
        userlink_e = l.find_element(By.XPATH,"./div/div/div[1]")
        userlink = userlink_e.find_element(By.XPATH,"./div/a").get_attribute("href")
        userimg = userlink_e.find_element(By.XPATH, "./div/a/div/img").get_attribute("src")
        userName = userlink_e.find_element(By.XPATH, "./div/div/div[1]/a").text
        #print(userlink,userimg,userName)
        vedio_e = l.find_element(By.XPATH,"./div/div/div[3]")
        #print(vedio_e.get_property("outerHTML"))
        id = vedio_e.find_element(By.XPATH,"./a").get_attribute("href")
        vedioimg = vedio_e.find_element(By.XPATH,"./img").get_attribute("src")
        vediotxt = vedio_e.find_element(By.XPATH,"./img").get_attribute("alt")
        #print(id,vedioimg,vediotxt)

        #视频无水印地址
        try:
            vediosrc = l.find_element(By.XPATH, "./div/div/div[4]/div/div/div[2]/div/div/xg-video-container/video/source[3]").get_attribute("src")
        except Exception as e:
            index+=1
            continue
        print(vediosrc)
        index+=1
        if id not in hascrawled:
            Data.append([id,userName,userimg,userlink,vedioimg,vediotxt,vediosrc])
            with open('aabb.csv', 'a+') as f:
                writer = csv.writer(f)
                writer.writerow([id,userName,userimg,userlink,vedioimg,vediotxt,vediosrc])
            wb = openpyxl.load_workbook('./resources.xlsx')
            sheet = wb['video']
            videoname = "cyf_"+id.split('/')[-1]+".mp4"
            download_videofile(vediosrc,videoname)
            sheet.append(['',ntoe[ind],"第"+ntoc[ind]+"批","第"+ntoc[ind]+"批",videoname,vediotxt,str(2014+ind)+"1010"])
            wb.save('./resources.xlsx')
driver.quit()
'''
