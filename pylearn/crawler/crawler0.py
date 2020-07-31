# -*- coding: utf-8 -*-
"""
Created on Sat Jun  1 20:11:06 2019

@author: YY
"""

from urllib.request import urlopen
import re
from bs4 import BeautifulSoup

# =============================================================================
# html = urlopen('https://morvanzhou.github.io/static/scraping/basic-structure.html').read().decode('utf-8')
# 
# #print(html)
# 
# #res = re.findall(r'<title>(.+?)</title>',html)
# #print('the title: ',res[0])
# 
# #res = re.findall(r'href="(.+?)"',html)
# #print('all_link',res)
# 
# soup = BeautifulSoup(html,features='lxml')
# #print(soup.h1)
# all_href = soup.find_all('a')
# all_href = [l['href'] for l in all_href]
# print(all_href)
# =============================================================================

# =============================================================================
# html = urlopen('https://morvanzhou.github.io/static/scraping/list.html').read().decode('utf-8')
# soup = BeautifulSoup(html,features='lxml')
# month = soup.find_all('li',{'class':'month'})
# for m in month:
#     print(m,'\t ',m.get_text())
# jan = soup.find('ul',{'class':'jan'})
# d_jan = jan.find_all('li')
# for day in d_jan:
#     print(day.get_text())
# =============================================================================

#print(re.search('1','21314'))

html = urlopen('https://morvanzhou.github.io/static/scraping/table.html') .read().decode('utf-8')
soup = BeautifulSoup(html,features='lxml')

img_links =  soup.find_all('img',{'src':re.compile('.*?\.jpg')})
for link in img_links:
    print(link['src'])
source_links = soup.find_all('a',{'href':re.compile(r'https://morvan\..*')})
for source in source_links:
    print(source['href'])
    
