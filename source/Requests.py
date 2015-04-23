# -*- coding: utf-8 -*-
import requests
#https://www.baidu.com/s?wd=API
#baseurl="https://www.baidu.com/s?"
payload={'var1':'mfc','var2': 'api'}
r=requests.get("https://www.zhihu.com")
print r.headers['content-type']
