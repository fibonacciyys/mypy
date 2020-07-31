# -*- coding: utf-8 -*-

ath=['x','y','z']
for i in range(3):
    for j in range(3):
        if i!=j:
            for k in range(3):
                if i!=k and j!=k:
                    if i!=0 and k!=0 and k!=2:
                        print('a--%c b--%c c--%c'%(ath[i],ath[j],ath[k]))