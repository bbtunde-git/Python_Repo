#!/usr/bin/env python
# coding: utf-8

# In[5]:


import urllib.request
import urllib.parse
from bs4 import BeautifulSoup

url='http://www.facebook.com?'

dict={'s':'gucci watch'}

headers={}
headers['User-Agent']='Mozilla/8.0'


get_data=urllib.parse.urlencode(dict)

get_data=get_data.encode('Utf-8')

get_url=urllib.request.Request(url,get_data, headers=headers)

req=urllib.request.urlopen(get_url).read()

print(req)


