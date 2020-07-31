#!C:\Anaconda3\python
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 28 19:55:02 2018

@author: YY
"""

import tkinter as tk

def hi():
    print('hi')

	
def main():
	win=tk.Tk()
	menubar=tk.Menu(win)
	filemenu=tk.Menu(menubar,tearoff=0)
	filemenu.add_command(label='open',command=hi)
	filemenu.add_command(label='save',command=hi)
	filemenu.add_separator
	filemenu.add_command(label='exit',command=win.destroy)
	menubar.add_cascade(label='File',menu=filemenu)
	editmenu=tk.Menu(menubar,tearoff=0)
	editmenu.add_command(label='cut',command=hi)
	editmenu.add_command(label='copy',command=hi)
	editmenu.add_command(label='paste',command=hi)
	menubar.add_cascade(label='Edit',menu=editmenu)

	win.config(menu=menubar)
	win.mainloop()
	
if __name__=='__main__':
	main()