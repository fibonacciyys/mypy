# -*- coding: utf-8 -*-

count=0

for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            if i!=j and j!=k and k!=i :
                print(str(i*100+j*10+k))
                count+=1
                
print("数量:"+str(count))