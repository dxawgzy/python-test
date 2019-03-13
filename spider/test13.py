#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'igis_gzy'

import requests
import time
from bs4 import BeautifulSoup

# import sys
# reload(sys)
# sys.setdefaultencoding('utf8')

# headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'}
# web_data = requests.get('http://newhouse.wuhan.fang.com/house/s/', headers=headers)
web_data = requests.get('http://newhouse.wuhan.fang.com/house/s/')
soup = BeautifulSoup(web_data.text, 'lxml')
links = soup.select('#newhouse_loupai_list > ul > li > div > div.nlc_details > div.house_value.clearfix > div > a')

# print(soup.prettify('gb2312'))
print(soup.prettify('utf8'))

def get_info(url):
    # web_data = requests.get(url, headers=headers)
    web_data = requests.get(url)
    soup = BeautifulSoup(web_data.text, 'lxml')
    try:
        tittles = soup.select('body > div.main-wrap > div.house-title > h1')
        print(tittles[0].string)
        print(tittles[0].get_text())
    except:
        print("异常")
    # print(tittles.get_text().strip())


# try:
    # res=requests.get('http://zhibohk.xs9999.com/', headers=header)
    # #print(res.text)
# except :
    # print('连接错误')
# if __name__ == '__main__':
#
#     for link in links:
#         href = link.get("href")
#         print(href)
        # get_info(href)
        # time.sleep(2)

