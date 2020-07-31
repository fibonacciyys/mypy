# -*- coding: utf-8 -*-

def fib(maxx):
    n,x,y=0,0,1
    while n<maxx:
        yield y
        x,y=y,x+y
        n+=1
        
m=fib(21)
next(m)
s=fib(22)
next(s)
next(s)
su=0
for i,j in zip(s,m):
    su+=i/j
print("sum={}".format(su))