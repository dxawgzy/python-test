#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'igis_gzy'

import requests
import time
from bs4 import BeautifulSoup

import sys
reload(sys)
sys.setdefaultencoding('utf8')

# headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'}
web_data = requests.get('http://zhibohk.xs9999.com/')
soup = BeautifulSoup(web_data.text, 'lxml')
# links = soup.select('#warp2 > div.LiveTeacher > div > ul > li:nth-of-type(1) > div.fl.teacher-mes > div.teacher-title > h3')
# print soup.prettify()
links = soup.select('.LiveTeacher')
print links
# print(links[0].get_text())


