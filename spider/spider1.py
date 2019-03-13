# -*- coding: utf-8 -*-
__author__ = 'igis_gzy'

from selenium.webdriver import FirefoxProfile
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import time
import re
import urllib
import math
import os

class Spider():

    def __init__(self, base_url):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("excludeSwitches", ["ignore-certificate-errors"])
        self.driver  = webdriver.Chrome(chrome_options=options)
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.base_url = base_url

    def get_one_page_pic(self, url, path):
        self.driver.get(url)
        # first = driver.find_element_by_xpath("//ul/li[1]/p[1]/a").get_attribute("href")
        # 获取当前页所有图片预览图的链接（使用find_elements，而不是find_element）
        index = self.driver.find_elements_by_xpath("//ul/li/p[1]/a")
        links = []
        for i in index:
            link = i.get_attribute("href")
            links.append(link)
        image = []
        for li in links:
            first1 = li.split('/')[-1]
            self.driver.get("https://car.autohome.com.cn/chezhan/photoshow/big/" + first1)
            img = self.driver.find_element_by_xpath("//div[2]/div/div/div[1]/div/img").get_attribute("src")
            image.append(img)
            filename = img.split('/')[-1]
            urllib.urlretrieve(img, '%s\\%s' % (path, filename))
        time.sleep(1)

    def get_all(self):
        self.driver.get(self.base_url)
        name = self.driver.find_element_by_xpath("//h2").text
        item = self.driver.find_element_by_xpath("//h2/span[1]").text
        path = "e:\\pic\\%s" % name.split()[0]  #h2标签会获取两行文字：奔驰S级(275张) 和 返回车展首页 现在取第一行
        os.mkdir(path)
        item_pattern = re.compile(r'\d+')
        total = re.search(item_pattern, item).group()
        page = int(math.ceil(float(total)/60))
        urls = [self.base_url]
        url1 = self.base_url.rstrip('.html') #移除url末尾的 .html 字段
        for pa in range(2, page+1):
            urlnew = url1 + '-%s.html' % pa
            urls.append(urlnew)
        # for url in urls:
        #     get_one_page_pic(url)
        return urls, path

if __name__ == "__main__":
    #只需更改如下首页base_url即可完成爬取
    # base_url = "https://car.autohome.com.cn/chezhan/exps104/59.html"
    base_url = "https://car.autohome.com.cn/chezhan/exps104/4785.html"
    sp = Spider(base_url)
    urls, path = sp.get_all()
    for url in urls:
        sp.get_one_page_pic(url, path)
    sp.driver.close()
    sp.driver.quit()
