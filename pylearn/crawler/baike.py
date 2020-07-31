# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 01:01:58 2019

@author: YY
"""

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import random

base_url = 'https://baike.baidu.com'
history = ['/item/%E7%BD%91%E7%BB%9C%E7%88%AC%E8%99%AB/5162711']
for i in range(20):
    html = urlopen(base_url + history[-1]).read().decode('utf-8')
    #print(html)
    soup = BeautifulSoup(html,features='lxml')
    print(soup.h1.get_text(),'\turl:',history[-1])
    sub_urls = soup.find_all('a',{'target':'_blank','href':re.compile('/item/(%.{2})+(/\d*)?$')})
#    for i in sub_urls:
#        print(i.get_text(),'\t',i['href'])
    if len(sub_urls) != 0:
        history.append(random.sample(sub_urls,1)[0]['href'])
    else:
        history.pop()