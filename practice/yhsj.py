# -*- coding: utf-8 -*-
"""
Created on Thu Jan  9 16:39:37 2020

@author: ReoNa
"""

def generate(numRows: int):
    re_li = [[1]]
    while numRows > 1:
        li =re_li[-1]
        x,y = li + [0],[0] + li
        re_li.append([sum(i) for i in zip(x,y)])
        numRows -= 1
    return re_li

print(generate(3))