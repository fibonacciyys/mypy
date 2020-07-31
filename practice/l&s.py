# -*- coding: utf-8 -*-
"""
Created on Thu Jan  9 16:09:29 2020

@author: ReoNa
"""

def countAndSay(n: int) -> str:
    re_strr = '1'
    while n > 1:
        num = 0
        strr = ''
        sub_char = re_strr[0]
        for j in re_strr + 'e':
            if j == sub_char:
                num += 1
            else:
                strr = strr + str(num) + sub_char
                num = 1
                sub_char = j
        re_strr = strr
        n -= 1
    return re_strr

for i in range(7):
    print(countAndSay(i+1))