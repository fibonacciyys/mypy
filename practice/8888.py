# -*- coding: utf-8 -*-
"""
Created on Fri May 18 12:48:08 2018

@author: YY
"""

def modd(x):
    while(x>9):
        s=str(x)
        i_l=map(lambda x:int(x),s)
        x=sum(i_l)
    return x
        
if __name__ == '__main__':
    print(modd(8888**8888))