# -*- coding: utf-8 -*-

def func(n):#阶乘generater
    p=1
    for i in range(1,n+2):
        yield p
        p*=i
        
def main():
    su=0
    g=func(20)
    next(g)
    for i in g:
        su+=i
    print("sum={}".format(su))
    
if __name__=="__main__":
    main()