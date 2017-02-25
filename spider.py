# -*- coding:utf-8 -*-
#爬虫模块常见：urllib,urllib2,re,bsp,requests,scrapy..

import urllib
import urllib2
import re

class Reptile:
    def __init__(self):
        self.pageIndex = 1 #页数
        self.userAgent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
        #usragent 对付反爬机制的网站，可以模拟用户操作
        self.headers = {'User-Agent':self.userAgent}
        self.stories = []       #空列表存储内容
        self.enable = False         #存放程序是否继续运行的变量

    #获取源码
    def getPage(self,pageIndex):
        try:
            url = 'http://www.qiushibaike.com/hot/page/' + str(pageIndex)   #页面+
            request = urllib2.Request(url,headers=self.headers)   #设置网站访问参数，headers头信息模仿模拟器
            response = urllib2.urlopen(request)    #打开网址
            pageCode = response.read()      #read()读取全部源码
            return pageCode
        except urllib2.URLError,e:
            print u'connect qiushibaike.com fail And ',e

    #获取到消化，阅读量，评论数
    def getPageItems(self,pageIndex):
        pageCode = self.getPage(pageIndex)  #调用获取页面代码方法
        if not pageCode:
            print "Load pageCode fail"
            return None
        pattern = re.compile('<h2>(.*?)</h2>.*?<div class="content">(.*?)</div>.*?<i class="number">(.*?)</i>.*?<i class="number">(.*?)</i>',re.S)
        #编译正则表达式，提高效率,re.S 匹配换行符
        #新手对于正则模糊，直接打开开发者模式COPY，注意/
        items = re.findall(pattern,pageCode)    #匹配返回列表的方式
        pageStories = []
        for item in items:
            it0 = item[1].replace('<span>','')
            it1 = it0.replace('</span>','')       #正文进行去node节点符号
            try:
                it2 = it1.replace('<br/>','')       #修改，对于可能出现空字符的node节点做选择处理
                pageStories.append([item[0], it2, item[2], item[3]])
            except:
                pass
            # pageStories.append([item[0],it,item[2],item[3]])    #index添加到新的列表
            finally:
                return pageStories

    #缓存
    def loadPage(self):
        if self.enable == True:
            if len(self.stories) < 2:
                pageStories = self.getPageItems(self.pageIndex)     #处理页面的调用
                if pageStories:
                    self.stories.append(pageStories)        #添加到准备好的空列表展示
                    self.pageIndex += 1                 # + 1

    #调用展示
    def getOneStory(self,pageStories,page):
        n = 0 #回车的次数初始化
        for story in pageStories:
            input = raw_input('')
            n += 1
            self.loadPage()     #调用加载处理的页面
            if input == 'Q' or input == 'q':  #按Q退出
                self.enable = False
                return
            print "Index page ->%d\twhich ->%s from ->%s\n\nNext is content:\n%s"%(page,n,story[0],story[1])
            print 'This massage has %s reading,And has %s comment.'%(story[2],story[3])
            print "click <enter> continue, or click <Q> or <q> to qiut."
    #开始方法
    def start(self):
        print "Script is spidering now,click <enter> to see, or click <Q> or <q> to qiut."
        self.enable = True
        self.loadPage()
        nowPage = 0 #控制当前读取的页数
        while self.enable:
            if len(self.stories) > 0:
                pageStories = self.stories[0]
                nowPage += 1
                del self.stories[0]
                self.getOneStory(pageStories,nowPage)

if __name__ == "__main__":
    spider = Reptile()
    spider.start()
