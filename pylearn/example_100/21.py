# -*- coding: utf-8 -*-

n = 1
for i in range(9,0,-1):
    n = (n+1)<<1 #二进制向左平移
print(n)