# -*- coding: utf-8 -*-

import os
import re
import time
import json
import platform
import requests
import html2text
#import ConfigParser
import string, urllib2
from bs4 import BeautifulSoup

#quora
#base_url="https://www.quora.com/search"

#zhihu
base_url="https://www.zhihu.com/search"
kw = raw_input("请输入关键字（多个关键字请以空格隔开）:".decode("utf-8").encode("gbk"))
print kw
kw=kw.decode("gbk").encode("utf-8")
print kw.decode("utf-8")

#kw="java"
keywords = kw.split()
print keywords
#zhihu
search_url=base_url+"?q=" + '+'.join(keywords) +"&type=question"

#quora
#search_url=base_url+"?q=" + '+'.join(keywords)

print search_url
#header={
		#'Host': "www.quora.com",
		#'User-Agent':"Mozilla/5.0 (Windows NT 5.1; rv:34.0) Gecko/20100101 Firefox/34.0",
		#'Referer':"https://www.quora.com/search"
		#}
#sName = string.zfill(1,2) + '.html'#自动填充成六位的文件名
#path=".././temp/"
#sName = raw_input('input filename: ')
#fName=path + sName
#if os.path.exists(path):
	#print "ERROR: '%s' already exists" %sName
#else:
	#break


#print '正在下载第'.decode('utf-8').encde('gbk')+ str(2) + '个网页，并将其存储为'.decode('utf-8').encode('gbk') + sName + '......'
#f = open(fName,'w+')

m = requests.get(search_url)
print m.text.decode("utf-8").encode("gbk")
#m = urllib2.urlopen(search_url)
#result=m.read()
#f.write(result)
#f.close()
#r=requests.get(search_url)
#print type(r.text)
#print r.text.decode('utf-8').encode('gbk')


#session = None
#global session
#cf=ConfigParser.ConfigParser()
#cf.read("config.ini")
#email = cf.get("info", "email")
#password = cf.get("info", "password")
#print password
#s = requests.session()
#login_data = {"email": email, "password": password, "passwordless":0}
#header = {
        #'User-Agent': "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:34.0) Gecko/20100101 Firefox/34.0",
        #'Host': "www.jianshu.com",
        #'Referer': "http://www.jianshu.com/sign_in",
        #'X-Requested-With': "XMLHttpRequest"
    #}
#r = s.post('http://www.jianshu.com/sessions', data = login_data, headers = header)
#r = s.post('https://www.quora.com/webnode2/server_call_POST?__instart__', data = login_data)
#print r
#if r.html()["r"] == 1:
        #raise Exception("login failed.")

