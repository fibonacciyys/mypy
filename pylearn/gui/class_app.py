# -*- coding: utf-8 -*-
"""
Created on Thu Jun 28 19:34:32 2018

@author: YY
"""

from tkinter import *
class App:
    def __init__(self,win):
        frame=Frame(win)
        frame.pack()
        self.button=Button(frame,text='Quit',fg='red',command=win.destroy)
        self.button.pack(side=LEFT)
        self.hi_btn=Button(frame,text='hello',command=self.say_hi)
        self.hi_btn.pack(side=LEFT)
        
    def say_hi(self):
        print('hello world')
        
win=Tk()
app=App(win)
win.mainloop()

