#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import time
from bs4 import BeautifulSoup

import sys
reload(sys)
sys.setdefaultencoding('utf8')

# headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'}
headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:54.0) Gecko/20100101 Firefox/54.0'}
# web_data = requests.get('http://bj.xiaozhu.com/', headers=headers)
web_data = requests.get('https://blog.csdn.net/tantexian/article/category/2393281')
soup = BeautifulSoup(web_data.text, 'lxml')
# links = soup.select('#page_list > ul > li > a')
links = soup.select('div > h4 > a')

def get_info(url):
    # wb_data = requests.get(url, headers=headers)
    wb_data = requests.get(url)
    soup = BeautifulSoup(wb_data.text, 'lxml')
    tittles = soup.select('h6')[1]
    print tittles.string


# try:
    # res=requests.get('http://zhibohk.xs9999.com/', headers=header)
    # #print(res.text)
# except :
    # print('连接错误')
if __name__ == '__main__':
    for link in links:
        time.sleep(1)
        href = link.get("href")
        print href
        time.sleep(2)
        get_info(href)
