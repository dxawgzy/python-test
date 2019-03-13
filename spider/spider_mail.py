#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'igis_gzy'

import urllib
import urllib2
import cookielib
import re

class Mail:

    def __init__(self):
        #登录URL
        self.loginUrl = 'https://mail.fiberhome.com/coremail/'
        #数据URL
        # self.receiveMailUrl = 'https://mail.fiberhome.com/coremail/XT3/mbox/list.jsp?sid=BAPehjkkoKtKoaJAWFkkMpkCyqgvfcMF&fid=1'
        # self.receiveMailUrl = 'https://mail.fiberhome.com/coremail/XT3/pab/main.jsp?sid=BAkghjkkkyUKoaXTtFkkMVGXjplZLPJF&order=FN'
        # 联系人列表 GET方法
        self.peopleUrl = 'https://mail.fiberhome.com/coremail/XT3/pab/main.jsp?sid=BAGWrjkkfDIhoakxXFkknqUoTQkbbPCF&order=FN'
        self.proxyURL = '10.89.151.102:3128'
        self.proxy = urllib2.ProxyHandler({'http':self.proxyURL})
        self.cookies = cookielib.CookieJar()
        self.postdata = urllib.urlencode({
            'locale': 'zh_CN',
            'uid': 'zygong',
            'nodetect': 'false',
            'domain': 'fiberhome.com',
            'password': 'dxaw271594',
            'action:login': ''
        })
        #构建opener
        # self.opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(self.cookies))
        self.opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(self.cookies),self.proxy,urllib2.HTTPHandler)

        self.header = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
            'Connection': 'keep-alive',
            # 'Host': 'mail.fiberhome.com',
            # 'Referer': 'https://mail.fiberhome.com/coremail/',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0'
        }

    #获取页面
    def getPage(self):
        request  = urllib2.Request(
            url = self.loginUrl,
            # data = self.postdata)
            data = self.postdata, headers=self.header)
        result = self.opener.open(request)
        # print result.read().decode('utf-8')

        sid = None
        for item in self.cookies:
            if item.name == 'Coremail.sid':
                sid = item.value
        peopleUrl = 'https://mail.fiberhome.com/coremail/XT3/pab/list.jsp?sid=%s&order=FN&pabType=&page_no=1' % sid
        peoplerequest = urllib2.Request(
            url = peopleUrl, headers=self.header
        )
        result = self.opener.open(peoplerequest)
        # print result.read().decode('utf-8')

        emailUrl = 'https://mail.fiberhome.com/coremail/XT3/mbox/getListDatas.jsp?sid=%s&fid=1&nav_type=system&inbox=true' % sid
        emailrequest = urllib2.Request(
            url = emailUrl, headers=self.header
        )
        result = self.opener.open(emailrequest)
        print result.read().decode('utf-8')
        return result.read().decode('utf-8')

    #提取页面上的每一条信息
    def getContent(self, page):
        # 邮箱联系人
        # pattern = re.compile('<td class="chkcol".*?><td class="crop" title="(.*?)".*?<td class="crop" title="(.*?)"',re.S)
        # items = re.findall(pattern, page)
        # contents = []
        # for item in items:
        #     content = {'people': 'null', 'email': 'null'}
        #     content['people'] = item[0]
        #     content['email'] = item[1]
        #     contents.append(content)
        # return contents

        # pattern = re.compile('<td class="crop td_from".*?><a ondblclick.*?>(.*?)</a></td><td class="flag".*?></td><td id="td_subject.*?<a ondblclick.*?>(.*?)</a>.*?</td><td.*?></td><td class="td_time".*?title="(.*?)"',re.S)
        pattern = re.compile('<td class="crop td_from".*?><a ondblclick.*?>(.*?)</a>',re.S)
        items = re.findall(pattern, page)
        contents = []
        # for item in items:
        for item in page:
            content = {'people': 'null', 'subject': 'null', 'time': 'null'}
            # content['people'] = item[0]
            # content['subject'] = item[1]
            # content['time'] = item[2]
            content['people'] = item['from']
            content['subject'] = item['subject']
            content['time'] = item['receivedDate']
            contents.append(content)
        return contents

    def start(self):
        indexPage = self.getPage()
        contents = self.getContent(indexPage)

        print u"开始写入任务数据"
        filename = u'email123.txt'
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
        #     cur.execute("INSERT INTO email(name, email) values(%s,%s)",
        #                 (item['people'], item['email']))
        #     cur.execute("INSERT INTO email(name, subject, time) values(%s,%s,%s)",
        #                 (item['people'], item['subject'], item['time']))
        # cur.close()
        # conn.commit()
        # conn.close()
        # print u"写入数据库完成"

sdu = Mail()
sdu.start()

