# -*- coding: utf-8 -*-
import math
def is_prime(n):
    if n<2:
        return False
    else:
        for i in range(2,int(math.sqrt(n))+1):
            if n%i==0:
                return False
    return True

def main():
    for i in range(101):
        if is_prime(i):
            print(i)

if __name__=="__main__":
    main()
    