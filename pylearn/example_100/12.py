# -*- coding: utf-8 -*-
import math
def is_prime(x):
    if x<2:
        return False
    else:
        for i in range(2,int(math.sqrt(x)+1)):
            if x % i ==0 :
                return False
        return True

def main():
    num=0
    for i in range(101,201):
        if is_prime(i):
            print(i)
            num+=1
    print("num:"+str(num))
            
if __name__=="__main__":
    main()