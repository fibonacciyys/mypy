# -*- coding: utf-8 -*-
"""
Created on Fri Feb  7 13:57:54 2020

@author: ReoNa
"""

s = "cabc"
uni = set(s)
set_ascii_li = sorted([ord(c) for c in uni])
res_ascii_li = []
lenn = len(set_ascii_li)
def min_str(s,iter = 0):
    print(iter)
    if iter == lenn:
        return True
    elif iter + len(s) < lenn:
        return False  
    for ascii in set_ascii_li:
        for i in range(len(s)):
            if ascii == ord(s[i]):
                res_ascii_li.append(ascii)
                ind = set_ascii_li.index(ascii)
                set_ascii_li.remove(ascii)
                if min_str(s[i+1:],iter+1):
                    return True
                res_ascii_li.pop()
                set_ascii_li.insert(ind,ascii)
    return False
min_str(s)
print(''.join([chr(ascii) for ascii in res_ascii_li]))