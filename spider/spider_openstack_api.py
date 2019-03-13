#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'igis_gzy'

import urllib2
import re


#处理页面标签类
class Tool:
    # #去除img标签,7位长空格
    # removeImg = re.compile('<img.*?>| {7}|')
    # #删除超链接标签
    # removeAddr = re.compile('<a.*?>|</a>')
    # #把换行的标签换为\n
    # replaceLine = re.compile('<tr>|<div>|</div>|</p>')
    # #将表格制表<td>替换为\t
    # replaceTD= re.compile('<td>')
    # #把段落开头换为\n加空两格
    # replacePara = re.compile('<p.*?>')
    # #将换行符或双换行符替换为\n
    # replaceBR = re.compile('<br><br>|<br>')
    # #将其余标签剔除
    # removeExtraTag = re.compile('<.*?>')
    removeTag = re.compile('<span class="path_parameter">')
    removeTag2 = re.compile('</span>')
    def replace(self,x):
        # x = re.sub(self.removeImg,"",x)
        # x = re.sub(self.removeAddr,"",x)
        # x = re.sub(self.replaceLine,"\n",x)
        # x = re.sub(self.replaceTD,"\t",x)
        # x = re.sub(self.replacePara,"\n    ",x)
        # x = re.sub(self.replaceBR,"\n",x)
        # x = re.sub(self.removeExtraTag,"",x)
        x = re.sub(self.removeTag, "", x)
        x = re.sub(self.removeTag2, "", x)
        return x.strip()   #strip()将前后多余内容删除


#爬虫类
class BDTB:

    #初始化，传入基地址，是否只看楼主的参数
    def __init__(self,baseUrl):
        #base链接地址
        self.baseURL = baseUrl
        #HTML标签剔除工具类对象
        self.tool = Tool()
        #全局file变量，文件写入操作对象
        self.file = None
        #默认的标题，如果没有成功获取到标题的话则会用这个标题
        self.defaultTitle = u"OpenStack API"

    #获取页面内容
    def getPage(self,url):
        try:
            request = urllib2.Request(url)
            response = urllib2.urlopen(request)
            #返回UTF-8格式编码内容
            return response.read().decode('utf-8')
        except urllib2.URLError, e:
            if hasattr(e,"reason"):
                print u"连接失败,错误原因",e.reason
                return None

    #获取标题
    def getTitle(self,page):
        #得到标题的正则表达式
        #<h1>Identity API v3 (CURRENT)<a class="headerlink" href="#identity-api-v3-current" title="Permalink to this headline">¶</a></h1>
        pattern = re.compile('<h1>(.*?)<a class="headerlink.*?>',re.S)
        result = re.search(pattern,page)
        if result:
            #如果存在，则返回标题
            return result.group(1).strip()
        else:
            return None

    #获取每一个API的内容,传入页面内容
    def getContent(self,page):
        pattern = re.compile('<div class="operation-grp.*?>(.*?)>detail</button>',re.S)
        items = re.findall(pattern,page)
        contents = []
        for item in items:
            content = {'method': 'null', 'url': 'null', 'function': 'null'}
            method_pattern = re.compile('<span class="label label-.*?>(.*?)</span>',re.S)
            content['method'] = re.search(method_pattern ,item).group(1).strip()
            url_pattern = re.compile('<div class="row col-md-12">(.*?)</div>',re.S)
            content['url'] = re.search(url_pattern ,item).group(1).strip()
            function_pattern = re.compile('<p class="url-subtitle">(.*?)</p>',re.S)
            content['function'] = re.search(function_pattern ,item).group(1).strip()
            #将文本进行去除标签处理，同时在前后加入换行符
            content['url'] = self.tool.replace(content['url'])
            contents.append(content)
        return contents

    def setFileTitle(self,title):
        #如果标题不是为None，即成功获取到标题
        if title is not None:
            self.file = open(title + ".txt","w+")
        else:
            self.file = open(self.defaultTitle + ".txt","w+")

    def start(self):
        indexPage = self.getPage(self.baseURL)  #获取页面HTML代码
        title = self.getTitle(indexPage)
        self.setFileTitle(title)
        try:
            print u"正在写入数据"
            contents = self.getContent(indexPage)
            self.file.write(str(contents))
        #出现写入异常
        except IOError,e:
            print u"写入异常，原因" + e.message
        finally:
            print u"写入任务完成"
        # print u"正在写入数据"
        # contents = self.getContent(indexPage)
        # filename = u'API爬取.txt'
        # with open(filename, 'w') as fp:
        #     fp.write(str(contents))
        # print u"写入任务完成"

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
        #     cur.execute("INSERT INTO openstack_api(method, url, function) values(%s,%s,%s)",
        #                 (item['method'], item['url'], item['function']))
        # cur.close()
        # conn.commit()
        # conn.close()
        # print u"写入数据库完成"

# baseURL = 'http://tieba.baidu.com/p/' + str(raw_input(u'http://tieba.baidu.com/p/'))
baseURL = 'https://developer.openstack.org/api-ref/identity/v3/'
bdtb = BDTB(baseURL)
bdtb.start()

