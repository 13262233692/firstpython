# -*- coding:utf-8 -*-


import time
import requests
import re
import json
import bs4
import os
import sys
from bs4 import BeautifulSoup
import urllib
index=0
def jyUrls(i):
    urls=list()
    for i in range(1,100):
        url="http://www.3jy.com/index/{0}.html".format(i)
        urls.append(url)
    return urls

def getWeb(url):
    #r = requests.get('http://www.3yj.com')
    html = requests.get(url, timeout=10).content.decode('utf-8')
    #html = r.text
    return html

def getString(html):
    soup=BeautifulSoup(html)
    div=list()
    for i in range(1,10):
        temp=soup.select("div[id=content-{0}]".format(i))
       # print(temp)
       ## temp1=temp[0]
       # print(type(temp1))
        div.append(temp)
    h2=list()
    pic=list()
    for j in div:
        j=j[0]
      #  print(type(j))
        #取文字
        flag=j.select("h2")
        flag=flag[0]
        h2.append(flag)
        #取图片链接
        flag=j.img
       # print(flag)
      #  print(type(flag))
        if flag!=None:
            flag1=flag['src']
            pic.append(flag1)
       # print(flag1)
    a=list()
    for j in h2:
        flag=j.select("a")
        flag=flag[0]
        a.append(flag)
    for j in a:
        print(j.string)

    for url in pic:
        global index
        if downImg(url, dirpath, str(index) + ".jpg"):
            index += 1
            print("已下载 %s 张" % index)



def downImg(imgUrl, dirpath, imgName):
    filename = os.path.join(dirpath, imgName)
    try:
        res = requests.get(imgUrl, timeout=15)
        if str(res.status_code)[0] == "4":
            print(str(res.status_code), ":" , imgUrl)
            return False
    except Exception as e:
        print("抛出异常", imgUrl)
        print(e)
        return False
    with open(filename, "wb") as f:
        f.write(res.content)
    return True



def mkDir(dirName):
    dirpath = os.path.join(sys.path[0], dirName)
    if not os.path.exists(dirpath):
        os.mkdir(dirpath)
    return dirpath


if __name__=='__main__':
    dirpath = mkDir("results")

    pic=list()
    urls=jyUrls(1)
    for url in urls:
        time.sleep(3)
        html=getWeb(url)
        print(url)
        pic=getString(html)
