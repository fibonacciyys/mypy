#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 28 18:36:47 2018

@author: YY
"""

from tkinter import *

def on_click():
    label['text']=text.get()

def hello():
    label['text']='Hello World'
    print('helloworld')
app=Tk(className='bitunion')
#app.title('YYs')
app.geometry('600x400')
label=Label(app)
label['text']='Interesting'
label.pack()
text=StringVar()
text.set('change to what')
entry=Entry(app)
entry['textvariable']=text
entry.pack()
button=Button(app)
button['text']='change'
button['command']=on_click
button.pack()
button1=Button(app,text='p_hello',command=hello)
button1.pack(expand=YES,fill=BOTH)
app.mainloop()