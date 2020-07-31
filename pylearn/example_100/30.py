# -*- coding: utf-8 -*-

def is_hws(n):
    ls=[]
    while(n):
        x=n%10
        ls.append(x)
        n//=10
    or_ls=ls[::-1]
    if or_ls==ls:
        return True
    else:
        return False
    
def main():
    n=int(input("请输入一个数:"))
    if is_hws(n):
        print("{}是回文数".format(n))
    else:
        print("{}不是回文数".format(n))
        
if __name__=="__main__":
    main()