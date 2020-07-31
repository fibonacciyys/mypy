# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 22:31:26 2019

@author: YY
"""
#strr = 'hello world!'
##for i in strr:
##    print(i)
#    
#for i in range(int(len(strr)/2)):
#    print(strr[i*2:i*2+2])



str_list = '零一二三四五六七八九'
ord_list = []
for strr in str_list:
    ord_list.append(ord(strr))
    
def a_num2str(num):
    return chr(ord_list[int(num)])

def num2str1(long_num):
    strr = ''
    for i in str(long_num):
        strr += a_num2str(i)
    return strr
def num2str2(long_num):
    strr = ''
    for i in map(a_num2str,list(str(long_num))):
        strr += i
    return(strr)
    
print(num2str1(43124142))
print(num2str2(43124142))