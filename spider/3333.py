# -*- coding: utf-8 -*-

import re
import urllib
import sys
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

#获取页面源码
def getHtml(url):
      page=urllib.urlopen(url)   # 打开页面
      html = page.read()       #获取目标页面的源码
      return html

#获取页面中的图片地址
def getImg(html):
      #reg=r'src="(.+?\.png)"'     #正则表达是筛选图片格式
      reg=r'src="(\/captcha\/image\/.+?)"'     #正则表达是筛选图片格式
      img = re.compile(reg)       #创建模式对象
      imglist = re.findall(img,html)   #解析页面源码获取图片列表
      #x=0
      for imgurl in imglist:
           try:
                imgurl1=url+imgurl      
                #由于获取的地址不带域名信息，所以拼接上域名
		x = imgurl.split("/")[3]
                urllib.urlretrieve(imgurl1,'%s.png' % x)  
                 # 保存图片，进行重命名
           except:
                print('Unexpected error:',sys.exc_info())
      return imglist

#调用方法
url = "https://10.127.4.153"
html = getHtml(url)
#print(html)
print(getImg(html))
