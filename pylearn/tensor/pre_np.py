# -*- coding: utf-8 -*-
"""
Created on Fri Jun 29 20:58:42 2018

@author: YY
"""

import numpy as np

data=[1,2,3,4,5,6]
x=np.array(data)
print(x)
print(x.dtype)
print(x[0:4:2])

data=[[1,2],[3,4],[5,6]]
x=np.array(data)
print(x)
print(x.ndim)#几维
print(x.shape)#nxn
print(x[:2,:1])

x=np.zeros((2,3))#shape
print(x)
#x=np.empty((3,4))
#print(x)

