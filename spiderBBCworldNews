  1 # -*- coding:utf-8 -*-
  2 #Author：李嘉艺
  3
  4 import urllib2
  5 import re
  6 import time
  7 from sys import exit
  8
  9
 10 print '获取中ing..........'
 11 agent_herf ='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
 12 try:
 13     f = urllib2.Request('http://www.bbc.com/zhongwen/simp/world',headers={'User-Agent':agent_herf}) #头部信息
 14     response = urllib2.urlopen(f)  # 打开网址
 15     pageCode = response.read()  # read()读取全部源码
 16     # print pageCode
 17 except:
 18     print '请确保您的电脑网络可翻墙，如有问题可咨询paul'
 19 patten = re.compile('simp/world-(.*?)" class=.*?title-text">(.*?)</span>.*?item__summary">(.*?)</p>',re.S)  #菜鸟式正则
 20 text = re.findall(patten,pageCode)          #匹配
 21
 22 name = raw_input("请问怎么称呼？")
 23 localtime = time.asctime( time.localtime(time.time()) )
 24
 25 if name:
 26     print '尊敬的%s(先生/女士)'%name
 27 else:
 28     print '先生/女士：今天是%s: '%localtime
 29
 30 print '为您播放今日BBC国际新闻前%s条信息:'%(len(text)-1)  #本来可以索引20条的  谁知道还存在反爬装置，等capable OK再搞
 31 print '过程点击回车键继续，输入q退出。'
 32 x = 0
 33 y = 0
 34 # print text
 35 for _ in range(len(text) - 1):
 36     input = raw_input('')
 37     if y == 1:      #存在第二条信息是瞎来的，索引去除
 38         y = 2
 39     print 'Massage<%d>'%int(x+1)
 40     print '%s:'%(text[x][1].decode('utf-8'))
 41     print '     -->>%s<<--'%(text[x][2].decode('utf-8'))
 42     print '         ____详情连接 : http://www.bbc.com/zhongwen/simp/world-'+text[y][0]
 43     x += 1
 44     y += 1
 45     if input == 'q':  # 按Q退出
                                                                                                                                                                   1,1           Top
