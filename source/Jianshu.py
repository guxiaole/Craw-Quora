# -*- coding: utf-8 -*-

import os
import re
import time
import json
import platform
import requests
import html2text
import ConfigParser
from bs4 import BeautifulSoup


#session = None
#global session
cf=ConfigParser.ConfigParser()
cf.read("config.ini")
email = cf.get("info", "email")
password = cf.get("info", "password")
#email="555555"
s = requests.session()
#m=s.get('http://www.jianshu.com/sign_in')
#print m
login_data = {"email": email, "password": password}
header = {
        'Host': "www.jianshu.com",
	'Origin': "http://www.jianshu.com",
	'Referer': "http://www.jianshu.com/sign_in",
        'User-Agent': "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.120 Safari/537.36"
        #'X-Requested-With': "XMLHttpRequest"
    }
r = s.post('http://www.jianshu.com/sessions', data = login_data, headers = header)
testurl=s.get('http://www.jianshu.com/subscription_notes')
print testurl.text
#if r.html()["r"] == 1:
        #raise Exception("login failed.")

