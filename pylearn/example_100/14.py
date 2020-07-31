# -*- coding: utf-8 -*-


def main() :
    n=int(input("请输入一个整数:"))
    print(str(n)+'=',end='')
    while(n!=1):
        for i in range(2,n+1):
            if n%i==0:
                n//=i
                if n!=1:
                    print("%d*"%i,end='')
                else:
                    print(i,end='')
                break
            
if __name__=="__main__":
    main()