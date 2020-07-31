# -*- coding: utf-8 -*-

def main():
    for n in range(1000):
        summ=0
        for i in range(1,n):
            if n%i==0:
                summ+=i
        if summ==n:
            print(n)

if __name__ == "__main__":
    main()
