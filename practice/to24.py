#!C:\Anaconda3\python
# -*- coding: utf-8 -*-


import tkinter as tk
import itertools
#def norepeated(li):
#    return len(list(set(li)))==4
one_line=1#输出一行开关
def t24(x1,x2,x3,x4):
    is_findd=0
    num=[x1,x2,x3,x4]
#    num_list=[[(n1,m1),(n2,m2),(n3,m3),(n4,m4)] for n1,m1 in enumerate(num) 
#        for n2,m2 in enumerate(num) for n3,m3 in enumerate(num) for n4,m4 in enumerate(num)]
#    num_list=list(filter(norepeated,num_list))
#    num_list=[[m1[0][1],m1[1][1],m1[2][1],m1[3][1]] for m1 in num_list]
    num_list=itertools.permutations(num,4)
    sym=['+','-','*','/']
    sym_list=[[n1,n2,n3] for n1 in sym for n2 in sym for n3 in sym]
    list_0_1=[0,1]
    is_add_lsit=[[n1,n2,n3] for n1 in list_0_1 for n2 in list_0_1 for n3 in list_0_1]
    for i in num_list:
        if is_findd and one_line:
            break
        for symm in sym_list:
            if is_findd and one_line:
                break
            for brac in is_add_lsit:
                if is_findd and one_line:
                    break
                s='({}'
                for x,item in enumerate(symm):
                    if is_findd and one_line:
                        break   
                    if brac[x]:
                        item1=')'+item+'('
                    else:
                        item1=item
                    if x==2:
                        s=s+item1+'{})'
                    else:
                        s=s+item1+'{}'
                s=s.format(*i)
                try:
                    if eval(s)==24:
                        print(s,'=24')
                        return s+'=24'
                        is_findd=1
                except:
                    pass
    if not is_findd:
        print('{},{},{},{}无法构成24点'.format(x1,x2,x3,x4))
        return '{},{},{},{}无法构成24点'.format(x1,x2,x3,x4)
#t24(5,5,5,1)
#t24(4,7,11,13)
#t24(7,7,7,7)
        
def main():
    def get_ans():
        s=entry.get()
        print(s)
        s=s.strip().split()  
        if len(s)==4:
            try:
                [int(x) for x in s]
                ans=t24(*s)
                strvar.set(ans)
                strvar2.set('')
            except:
                strvar.set('错误输入')
                strvar2.set('')
        else:
            strvar.set('输入数量错误')
            strvar2.set('')
        
    def enter_to_ans(event):
        if event.char=='\r':
            get_ans()
    
    app=tk.Tk()
    app.geometry('300x130')
    app.title('超级24点解答')
    frame=tk.Frame(app)
    frame.pack()
    label1=tk.Label(frame,text='输入4数字后按enter')
    label1.pack()
    strvar=tk.StringVar()
    strvar.set('输入4个数')
    strvar2=tk.StringVar()
    entry=tk.Entry(frame,textvariable=strvar2)
    entry.bind('<Key>',enter_to_ans)
    entry.pack()
    entry.focus_set
    label2=tk.Label(frame,textvariable=strvar)
    label2.pack()
    button=tk.Button(frame,text='确认',command=get_ans)
    button.pack()
    app.mainloop()
    
if __name__=='__main__':
    main()
    