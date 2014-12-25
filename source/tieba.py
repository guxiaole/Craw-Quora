# -*- coding: utf-8 -*-
#---------------------------------------
#   程序：百度贴吧爬虫
#   版本：0.1
#   作者：why
#   日期：2013-05-14
#   语言：Python 2.7
#   操作：输入带分页的地址，去掉最后面的数字，设置一下起始页数和终点页数。
#   功能：下载对应页码内的所有页面并存储为html文件。
#---------------------------------------
 
import string, urllib2
 
#定义百度函数
def baidu_tieba(url): #for i in range(begin_page, end_page+1):
        sName = string.zfill(1,2) + '.html'#自动填充成六位的文件名
        print '正在下载第' + str(1) + '个网页，并将其存储为' + sName + '......'
        f = open(sName,'w+')
	url='http://www.baidu.com/'
	url='http://www.jianshu.com/'
	url='http://www.15yan.com/'
        m = urllib2.urlopen(url)
	result=m.read()
        f.write(result)
        f.close()
 
 
#-------- 在这里输入参数 ------------------

bdurl = 'http://www.15yan.com/topic/bian-ji-tui-jian/'
#iPostBegin = 1
#iPostEnd = 10

#bdurl = str(raw_input(u'adder\n'))
#begin_page = int(raw_input(u'beginnum \n'))
#end_page = int(raw_input(u'end_page \n'))
#-------- 在这里输入参数 ------------------
 

#调用
baidu_tieba(bdurl)
