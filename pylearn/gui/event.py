# -*- coding: utf-8 -*-
"""
Created on Fri Jun 29 21:43:11 2018

@author: YY
"""

from tkinter import *

root=Tk()

def callback(event):
    print('click at:',event.x,event.y)
    
def key(event):
    print('press:',repr(event.char))

def get_24(event):
    if event.char=='\r':
        print('content:',entry.get())
    
#    print(event.char=='\r')

frame=Frame(root,width=100,height=100)
frame.bind('<Key>',key)
frame.bind('<Button-1>',callback)

frame.pack()
text=StringVar()
entry=Entry(frame,textvariable=text)
entry.bind('<Key>',get_24)

entry.pack()


root.mainloop()