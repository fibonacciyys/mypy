# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 23:58:25 2019

@author: YY
"""

import requests
import webbrowser 

param = {'wd':'python'}
r = requests.get('http://www.baidu.com/s',params=param)
print(r.url)
webbrowser.open(r.url)