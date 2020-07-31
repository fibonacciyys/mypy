# -*- coding: utf-8 -*-
"""
Created on Thu Jun 28 20:22:05 2018

@author: YY
"""

from tkinter import *
import tkinter.messagebox as messagebox

#frame=Frame()
#frame.mainloop()

class Application(Frame):
    def __init__(self,master=None):
        Frame.__init__(self,master)
        self.pack()
        self.createWidgets()
        
    def createWidgets(self):
        self.nameinput=Entry(self)
        self.nameinput.pack()
        self.alertbtn=Button(self,text='hello',command=self.hello)
        self.alertbtn.pack()
        
    def hello(self):
        name=self.nameinput.get() or 'world'
        messagebox.showinfo('Msg','hello,%s'%name)
        
app=Application()
app.master.title='YYs'
app.mainloop()