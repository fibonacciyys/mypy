# -*- coding: utf-8 -*-
"""
Created on Sat Jun  9 20:20:48 2018

@author: YY

据说此题源于1981年柏林的德国逻辑思考学院，它是由爱因斯坦在20世纪初提出的：

　　1.在一条街上，有5座房子，喷了5种颜色。

　　2.每个房里住着不同国籍的人。

　　3.每个人喝不同的饮料，抽不同品牌的香烟，养不同的宠物。

　　其中：

　　1.英国人住红色房子

　　2.瑞典人养狗

　　3.丹麦人喝茶

　　4.绿色房子在白色房子左面(并相邻)

　　5.绿色房子主人喝咖啡

　　6.抽 Pall Mall 香烟的人养鸟

　　7.黄色房子主人抽 Dunhill 香烟

　　8.住在中间房子的人喝牛奶

　　9.挪威人住第一间房(左起第一间)

　　10.抽 Blends 香烟的人住在养猫的人隔壁

　　11.养马的人住抽 Dunhill 香烟的人隔壁

　　12.抽 Blue Master 的人喝啤酒

　　13.德国人抽 Prince 香烟

　　14.挪威人住蓝色房子隔壁

　　15.抽 Blends 香烟的人有一个喝水的邻居

　　问题是：谁养鱼?

"""

import itertools,gc,os

def test1(li):
    return li[1].index('British')==li[0].index('red')

def test2(li):
    return li[1].index('Swedish')==li[4].index('dog')

def test3(li):
    return li[1].index('Dane')==li[2].index('tea')

def test4(li):
    return li[0].index('green')==li[0].index('white')-1

def test5(li):
    return li[0].index('green')==li[2].index('coffee')

def test6(li):
    return li[3].index('Pall Mall')==li[4].index('bird')

def test7(li):
    return li[0].index('yellow')==li[3].index('Dunhill')

def test8(li):
    return li[2].index('milk')==2

def test9(li):
    return li[1].index('Norwegian')==0

def test10(li):
    return abs(li[3].index('Blends')-li[4].index('cat'))==1

def test11(li):
    return abs(li[4].index('horse')-li[3].index('Dunhill'))==1

def test12(li):
    return li[3].index('Blue Master')==li[2].index('beer')

def test13(li):
    return li[1].index('German')==li[3].index('Prince')

def test14(li):
    return abs(li[1].index('Norwegian')-li[0].index('blue'))==1

def test15(li):
    return abs(li[3].index('Blends')-li[2].index('water'))==1

def main():
    color=['yellow','blue','red','green','white']#0
    nation=['Norwegian','Dane','British','German','Swedish']#1
    drinks=['water','tea','milk','coffee','beer']#2
    cigarette=['Dunhill','Blends','Pall Mall','Prince','Blue Master']#3
    pets=['dog','cat','horse','bird','fish']#4 正确答案时该列表为['cat','horse','bird','fish','dog'](为演示效果and节约时间)
    color_list=list(itertools.permutations(color,5))
    nation_list=list(itertools.permutations(nation,5))
    drinks_list=list(itertools.permutations(drinks,5))
    cigarette_list=list(itertools.permutations(cigarette,5))
    pets_list=list(itertools.permutations(pets,5))
    summ=0
    conti=1
    for co in color_list:
        if not conti:
            break
        for na in nation_list:
            if not conti:
                break
            for dr in drinks_list:
                if not conti:
                    break
                for ci in cigarette_list:
                    if not conti:
                        break
                    for pe in pets_list:
                        if not conti:
                            break
                        total=[co,na,dr,ci,pe]
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
                                test10,
                                test11,
                                test12,
                                test13,
                                test14,
                                test15]
                        flags=1
                        for f in filter_list:
                            if not flags:
                                summ+=1
                                print(summ)
                                os.system('cls')
                                del total
                                break
                            if not f(total):
                                flags=0
                        if flags:
                            print(total)
                            conti=0
                            gc.collect()
                        

if __name__=='__main__':
    main()
    
    
    
    
    