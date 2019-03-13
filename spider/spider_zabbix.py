#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'igis_gzy'

import urllib
import urllib2
import cookielib
import re
import xlwt
import xlrd

class Zabbix:

    def __init__(self):
        #登录URL
        # http://10.22.20.84:10080/zabbix
        self.loginUrl = 'http://10.22.20.84:10080/zabbix/index.php'
        self.dataUrl = 'http://10.22.20.84:10080/zabbix/latest.php?ddreset=1'
        self.proxyURL = '10.89.151.102:3128'
        self.proxy = urllib2.ProxyHandler({'http':self.proxyURL})
        self.cookies = cookielib.CookieJar()
        self.postdata = urllib.urlencode({
            'form_refresh':	'1',
            'name':	'admin',
            'password': 'zabbix',
            'autologin': '1',
            'enter': 'Sign in'
        })
        self.header = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
            'Connection': 'keep-alive',
            # 'Cookie': 'PHPSESSID=amoss7o5nptgavi1ss83snhuj4',
            'Host': '10.22.20.84:10080',
            'Referer': 'http://10.22.20.84:10080/zabbix/index.php',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0'
        }
        #构建opener
        # self.opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(self.cookies))
        self.opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(self.cookies),self.proxy,urllib2.HTTPHandler)

    #获取数据HTML页面
    def getPage(self):
        request  = urllib2.Request(
            url = self.loginUrl,
            data = self.postdata, headers = self.header)
            # data = self.postdata)
        result = self.opener.open(request)
        result = self.opener.open(self.dataUrl)
        # print result.read().decode('utf-8')
        return result.read().decode('utf-8')

    #提取页面上的每一条信息
    def getContent(self, page):
        pattern = re.compile('<tr parent_app_id.*?>(.*?)</tr>',re.S)
        items = re.findall(pattern, page)
        contents = []
        for item in items:
            content = {'item': 'null', 'value': 'null', 'time': 'null'}
            item_pattern = re.compile('<input.*?<td>(.*?)</td><td>(.*?)</td><td>(.*?)</td>',re.S)
            content['item'] = re.search(item_pattern, item).group(1).strip()
            content['value'] = re.search(item_pattern, item).group(3).strip()
            content['time'] = re.search(item_pattern, item).group(2).strip()
            contents.append(content)
        return contents
        # 过滤方法二：此种方法可能会带来垃圾数据（可能其他数据也有满足如下正则要求）
        # pattern = re.compile('<input.*?<td>(.*?)</td><td>(.*?)</td><td>(.*?)</td>',re.S)
        # items = re.findall(pattern, page)
        # contents = []
        # for item in items:
        #     content = {'item': 'null', 'value': 'null', 'time': 'null'}
        #     content['item'] = item[0]
        #     content['value'] = item[2]
        #     content['time'] = item[1]
        #     contents.append(content)
        # return contents

    def start(self):
        indexPage = self.getPage()
        contents = self.getContent(indexPage)

        print u"开始写入任务数据"
        filename = u'Zabbix12344.txt'
        with open(filename, 'w') as fp:
            fp.write(str(contents))
        print u"写入任务完成"

        # print u"开始写入数据库"
        # import MySQLdb
        # conn = MySQLdb.connect(
        #     host='127.0.0.1',
        #     port=3306,
        #     user='root',
        #     passwd='123456',
        #     db='test1',
        #     charset='utf8')
        # cur = conn.cursor()
        # for item in contents:
        #     cur.execute("INSERT INTO zabbix_item_data(item, value, time) values(%s,%s,%s)",
        #                 (item['item'], item['value'], item['time']))
        # cur.close()
        # conn.commit()
        # conn.close()
        # print u"写入数据库完成"

        # print u"开始写入excel"
        # w = xlwt.Workbook()
        # sheet1 = w.add_sheet(u'Zabbix-item')
        # row0 = [u'item', u'value', u'time']
        # #生成第一行
        # for i in range(0,len(row0)):
        #     sheet1.write(0, i, row0[i])
        # #写入item数据
        # for i in range(0, len(contents)):
        #     sheet1.write(i+1, 0, contents[i]['item'])
        #     sheet1.write(i+1, 1, contents[i]['value'])
        #     sheet1.write(i+1, 2, contents[i]['time'])
        # w.save('zabbix.xls')
        # print u"写入excel完成"


sdu = Zabbix()
sdu.start()


# import pdb
# pdb.set_trace()


