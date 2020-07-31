# -*- coding: utf-8 -*-
"""
Created on Sun Dec 30 16:05:40 2018

@author: YY

作者：杨航锋
链接：https://www.zhihu.com/question/271643290/answer/362608527
来源：知乎
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""



import turtle
import random
from turtle import *
from time import sleep

t = turtle.Turtle()
w = turtle.Screen()


def tree(branchLen, t):
    if branchLen > 3:
        if 8 <= branchLen <= 12:
            if random.randint(0, 2) == 0:
                t.color('snow')
            else:
                t.color('lightcoral')
            t.pensize(branchLen / 3)
        elif branchLen < 8:
            if random.randint(0, 1) == 0:
                t.color('snow')
            else:
                t.color('lightcoral')
            t.pensize(branchLen / 2)
        else:
            t.color('sienna')
            t.pensize(branchLen / 10)

        t.forward(branchLen)
        a = 1.5 * random.random()
        t.right(20*a)
        b = 1.5 * random.random()
        tree(branchLen-10*b, t)
        t.left(40*a)
        tree(branchLen-10*b, t)
        t.right(20*a)
        t.up()
        t.backward(branchLen)
        t.down()


def petal(m, t):  # 树下花瓣
    for i in range(m):
        a = 200 - 400 * random.random()
        b = 10 - 20 * random.random()
        t.up()
        t.forward(b)
        t.left(90)
        t.forward(a)
        t.down()
        t.color("lightcoral")
        t.circle(1)
        t.up()
        t.backward(a)
        t.right(90)
        t.backward(b)


def main():
    t = turtle.Turtle()
    myWin = turtle.Screen()
    getscreen().tracer(5, 0)
    turtle.screensize(bg='wheat')
    t.left(90)
    t.up()
    t.backward(150)
    t.down()
    t.color('sienna')
    tree(60, t)
    petal(100, t)

    myWin.exitonclick()


main()