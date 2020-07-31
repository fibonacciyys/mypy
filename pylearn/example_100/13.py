# -*- coding: utf-8 -*-

def is_sxhs(x):
    i=x%10
    ii=(x//10)%10
    iii=x//100
    if x==iii**3+ii**3+i**3:
        return True
    else:
        return False

def main():
    count=0
    for i in range(100,1000):
        if is_sxhs(i):
            print(i)
            count+=1
    print(count)


if __name__ == "__main__":
    main()