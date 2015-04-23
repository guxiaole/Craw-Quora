# -*- coding: utf-8 -*-
import re
import urllib2
from BeautifulSoup import BeautifulSoup
 
doc = urllib2.urlopen("http://www.zhihu.com/question/27252710")
soup = BeautifulSoup(doc)
#text=soup.p.getText()
text=soup.getText()
text=text.decode("utf-8").encode("gbk")
print text
#print soup.findAll(text=re.compile("onerror"))
#for tag in soup.findAll(True):
    #print(tag.name)
#print soup.h2.next_sibling

#m=soup.findAll('h2')
#print m[0]
#print m(0).string

#print soup.find_all('h2')
#print soup.h2.string
#print soup.body.h2.string
#print soup.title.string

#print type(soup.title)
#print soup.head.title.contents
#print (soup.prettify()).encode("gbk")
#print soup.originalEncoding

#sibling_soup = BeautifulSoup("<a><b>text1</b><c>text2</c></b></a>")
#print(sibling_soup.prettify())
