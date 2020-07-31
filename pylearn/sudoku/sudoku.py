# -*- coding: utf-8 -*-
"""
Created on Wed Feb  5 19:07:47 2020

@author: ReoNa
"""

import tkinter as tk
import time

class Sudoku(object):
    def __init__(self):
        self.sudoku = [['.']*9 for _ in range(9)]
        self.row = [set(range(1, 10)) for _ in range(9)]  # 行剩余可用数字
        self.col = [set(range(1, 10)) for _ in range(9)]  # 列剩余可用数字
        self.block = [set(range(1, 10)) for _ in range(9)]  # 块剩余可用数字
        self.empty = [] # 待填格位置
        self.str_set = {}
        self.entry_set = {}
        self.duration = None
        self.app = None
        self.button_y = 650
        self.button_x = 170
        self.is_cancel = 0
        self.cancel_sudoku = [['.']*9 for _ in range(9)]
        
    def get_ui(self):
        self.app=tk.Tk()
        self.app.geometry('850x750')
        self.app.title('sudoku')
        for i in range(9):
            for j in range(9):
                ij = str(i) + str(j)
                self.str_set[ij]=tk.StringVar()
                self.entry_set[ij]=tk.Entry(self.app,
                              font = 'Helvetica 25 bold',
                              width=3,
                              textvariable=self.str_set[ij],
                              justify='center')
                self.entry_set[ij].place(y = 50+(i+i//3)*50,x = 50+(j+j//3)*70)
        label = tk.Label(self.app,text='运行间隔(ms):')
        label.place(x = self.button_x + 50,y=self.button_y)
        self.duration = tk.StringVar()
        self.duration.set('0')
        entry = tk.Entry(self.app,width=5,textvariable=self.duration)
        entry.place(x = self.button_x + 150,y=self.button_y)
        button0=tk.Button(self.app,text='例子',command=self.set_example)
        button0.place(x = self.button_x + 200,y=self.button_y)
        button1=tk.Button(self.app,text='确认',command=self.solveSudoku)
        button1.place(x = self.button_x + 250,y=self.button_y)
        self.app.bind('<Return>',self.solveSudoku)
        button2=tk.Button(self.app,text='清空',command=self.clean)
        button2.place(x = self.button_x + 300,y=self.button_y)
        button3=tk.Button(self.app,text='打印',command=self.print_sudoku)
        button3.place(x = self.button_x + 350,y=self.button_y)
        button4=tk.Button(self.app,text='取消',command=self.cancel)
        button4.place(x = self.button_x + 400,y=self.button_y)
        self.app.mainloop()
        
    def print_sudoku(self):
        self.update()
        print(self.sudoku)
        
    def cancel(self):
        self.is_cancel = 1
        self.clean()
        for i in range(9):
            for j in range(9):
                if not self.cancel_sudoku[i][j] == '.':
                    self.str_set[str(i) + str(j)].set(self.cancel_sudoku[i][j])
        
    def set_example(self):
        eg = [['6', '7', '.', '.', '.', '.', '.', '.', '.'], 
              ['.', '.', '.', '.', '.', '6', '.', '7', '3'], 
              ['.', '.', '3', '5', '1', '.', '.', '2', '9'], 
              ['.', '1', '.', '.', '5', '.', '.', '.', '2'], 
              ['.', '.', '.', '6', '.', '2', '.', '.', '.'], 
              ['5', '.', '.', '.', '7', '.', '.', '4', '.'], 
              ['1', '6', '.', '.', '3', '5', '2', '.', '.'], 
              ['7', '5', '.', '4', '.', '.', '.', '.', '.'], 
              ['.', '.', '.', '.', '.', '.', '.', '9', '7']]
        self.clean()
        for i in range(9):
            for j in range(9):
                if not eg[i][j] == '.':
                    self.str_set[str(i) + str(j)].set(eg[i][j])

    def clean(self):
        for strvar in self.str_set.values():
            strvar.set('')
        for entry in self.entry_set.values():
            entry.configure(fg='black')
        
    def backtrack(self,iter=0):
        if iter == len(self.empty):  # 处理完empty代表找到了答案
            return True
        i, j = self.empty[iter]
        b = (i // 3)*3 + j // 3
        for val in self.row[i] & self.col[j] & self.block[b]:
            if self.is_cancel:
                self.is_cancel = 0
                raise Exception('cancel')
            try:
                time.sleep(0.001*int(self.duration.get()))
            except:
                time.sleep(0.5)
            self.row[i].remove(val)
            self.col[j].remove(val)
            self.block[b].remove(val)
            self.sudoku[i][j] = str(val)
            self.str_set[str(i)+str(j)].set(str(val))
            self.app.update()
            if self.backtrack(iter+1):
                return True
            self.row[i].add(val)  # 回溯
            self.col[j].add(val)
            self.block[b].add(val)
            self.sudoku[i][j] = '.'
            self.str_set[str(i)+str(j)].set('')
        return False
        
    def update(self):
        self.sudoku = [['.']*9 for _ in range(9)]
        for i in range(9):
            for j in range(9):
                ij = str(i) + str(j)
                strr = self.str_set[ij].get()
                if not strr == '':
                    self.sudoku[i][j] = strr
                    self.cancel_sudoku[i][j] = strr
                    self.entry_set[ij].configure(fg='black')
                else:
                    self.entry_set[ij].configure(fg='red')

    def solveSudoku(self,*argvs):
        self.sudoku = [['.']*9 for _ in range(9)]
        self.cancel_sudoku = [['.']*9 for _ in range(9)]
        self.row = [set(range(1, 10)) for _ in range(9)]  # 行剩余可用数字
        self.col = [set(range(1, 10)) for _ in range(9)]  # 列剩余可用数字
        self.block = [set(range(1, 10)) for _ in range(9)]  # 块剩余可用数字
        self.empty = []
        self.update()
        self.is_cancel = 0
        for i in range(9):
            for j in range(9):
                if self.sudoku[i][j] != '.':  # 更新可用数字
                    val = int(self.sudoku[i][j])
                    self.row[i].remove(val)
                    self.col[j].remove(val)
                    self.block[(i // 3)*3 + j // 3].remove(val)
                else:
                    self.empty.append((i, j))
        self.backtrack()

if __name__ =='__main__':
    sudoku1 = Sudoku()
    sudoku1.get_ui()