# -*- coding: utf-8 -*-
"""
Created on Thu Jun 21 20:01:29 2018

@author: YY
"""
import math

def iter_lambda(x):
    return 1/(2*math.log(188361*x,10)-0.8)

def get_lambda():
    x=1
    while abs(iter_lambda(x)-x)>0.0000001:
        x=iter_lambda(x)
    return x

def main():
    lamb=get_lambda()
    print(lamb)
    
if __name__ == '__main__':
    main()