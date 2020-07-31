# -*- coding: utf-8 -*-
"""
Created on Wed May 16 17:23:07 2018

@author: YY
"""

import turtle as t

t.setup(800,400)
t.ondrag(t.goto)
t.colormode(255)
t.shape('turtle')
t.speed(3)
t.pendown()
t.begin_fill#t.fill(True)
for i in range(3):
    t.forward(100)
    t.left(120)
t.end_fill
t.penup()
t.done()