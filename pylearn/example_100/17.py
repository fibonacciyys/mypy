# -*- coding: utf-8 -*-

import string
def main():
    letter=0
    digit=0
    space=0
    other=0
    strr=input("请输入要检测的字符串:")
    for c in strr:
        if c.isalpha():
            letter+=1
        elif c.isdigit():
            digit+=1
        elif c.isspace():
            space+=1
        else:
            other+=1
    print("%d %d %d %d"%(letter,digit,space,other))
    
if __name__ == "__main__" :
    main()