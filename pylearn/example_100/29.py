# -*- coding: utf-8 -*-

def main():
    n=int(input("请输入一个正整数:"))
    cut=0
    ls=[]
    while(n):
        x=n%10
        ls.append(x)
        n//=10
        cut+=1
    ls=ls[::-1]
    print((ls,cut))

if __name__=="__main__":
    main()