# -*- coding: utf-8 -*-
"""
Created on Thu Jun  7 17:39:37 2018

@author: YY
"""

li=[2,3,4]
for i,x in enumerate(li):
    if i==0 and x==2: #不能用i==0 & x==2 可用(i==0) & (x==2) 运算符等级高于== &:位运算符
        print(i,x,'depart')
    if (i,x)==(0,2):
        print(i,x,'together')