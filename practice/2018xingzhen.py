# -*- coding: utf-8 -*-
"""
Created on Sat Jun  9 16:42:28 2018

@author: YY
"""

import gc,os

def test1(li):
    return True

def test2(li):
    suit_dict={
            1:3,
            2:4,
            3:1,
            4:2}
    ans=suit_dict[li[2]]
    return ans==li[5]

def test3(li):
    suit_dict={
            1:3,
            2:6,
            3:2,
            4:4}
    four_ans=[li[3],li[6],li[2],li[4]]
    ans=suit_dict[li[3]]
    four_ans.remove(li[ans])
    return li[ans] not in four_ans

def test4(li):
    suit_dict={
            1:(1,5),
            2:(2,7),
            3:(1,9),
            4:(6,10)}
    ans=suit_dict[li[4]]
    return li[ans[0]]==li[ans[1]]

def test5(li):
    suit_dict={
            1:8,
            2:4,
            3:9,
            4:7}
    ans=suit_dict[li[5]]
    return li[ans]==li[5]

def test6(li):
    suit_dict={
            1:(2,4),
            2:(1,6),
            3:(3,10),
            4:(5,9)}
    ans=suit_dict[li[6]]
    return li[8]==li[ans[0]]==li[ans[1]]

def test7(li):
    suit_dict={
            1:3,
            2:2,
            3:1,
            4:4}
    x1,x2,x3,x4=li.count(1),li.count(2),li.count(3),li.count(4)
    min_sel=min(x1,x2,x3,x4)
    ans=suit_dict[li[7]]
    return min_sel==li.count(ans)

def test8(li):
    suit_dict={
            1:7,
            2:5,
            3:2,
            4:10}
    ans=suit_dict[li[8]]
    return (li[1]-li[ans])**2>2

def test9(li):
    suit_dict={
            1:6,
            2:10,
            3:2,
            4:9}
    ans=suit_dict[li[9]]
    prop1=li[1]==li[6]
    prop2=li[ans]==li[5]
    return prop1!=prop2

def test10(li):
    suit_dict={
            1:3,
            2:2,
            3:4,
            4:1}
    ans=suit_dict[li[10]]
    x1,x2,x3,x4=li.count(1),li.count(2),li.count(3),li.count(4)
    min_sel=min(x1,x2,x3,x4)
    max_sel=max(x1,x2,x3,x4)
    result0=max_sel-min_sel
    return ans==result0
        
def chan2(num):
    if num:
        return chr(64+num)
    else:
        return '答案'

def main():
    ans=[1,2,3,4]
    for x1 in ans:
        for x2 in ans:
            for x3 in ans:
                for x4 in ans:
                    for x5 in ans:
                        for x6 in ans:
                            for x7 in ans:
                                for x8 in ans:
                                    for x9 in ans:
                                        for x10 in ans:
                                            ans_list=[0,x1,x2,x3,x4,x5,x6,x7,x8,x9,x10]
                                            filter_list=[
                                                    test1,
                                                    test2,
                                                    test3,
                                                    test4,
                                                    test5,
                                                    test6,
                                                    test7,
                                                    test8,
                                                    test9,
                                                    test10]
                                            flags=1
                                            for f in filter_list:
                                                if not flags:
                                                    del ans_list
                                                    break
                                                if not f(ans_list):
                                                    flags=0
                                            if flags:
                                                ans_list=[chan2(ans) for ans in ans_list]
                                                print(list(enumerate(ans_list)))
    gc.collect()
if __name__=='__main__':
    main()
    
