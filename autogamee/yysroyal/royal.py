#C:\Anaconda3\python
#\usr\bin\env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 29 18:58:55 2018

@author: YY
init_window:(211, 0, 45, 255)1370,870,1580,957(22, 32, 46, 255)1406,910,1554,932
jump_window:(50, 137, 209, 255)1720,55,1877,90
other_jump:(48, 132, 200, 255)
no_press:(34, 38, 46, 255)
end:(9, 39, 64, 255)1516,937,1644,1000
again:(28, 28, 43, 255)1516,937,1644,1000
"""

from interactt import random_tap,get_pic
from multiprocessing import Process,Queue
from PIL import Image
#import time
import cv2
import subprocess
from io import BytesIO

def get_screen():
    process = subprocess.Popen('adb shell screencap -p',shell=True, stdout=subprocess.PIPE)
    binary_screenshot = process.stdout.read()
    binary_screenshot = binary_screenshot.replace(b'\r\n', b'\n')
    im=Image.open(BytesIO(binary_screenshot))
    return im

def get_statement(q):
#    get_pic('risk')
#    im=Image.open('risk.png')
#    pixx=im.load()
#    try:
#        tup=pixx[1840,72]
#    except:
#        tup=(0,0,0,0)
    im=get_screen()
    try:
        tup=im.getpixel((1840,72))
    except:
        print('不是横屏')
    im.close()
    print(tup)
    if tup==(22, 32, 47, 255) or tup==(21, 33, 46, 255) or tup==(21, 34, 46, 255):
        q.put(1)
        print('闯关')
        return 1
    elif tup[2]>100:
        q.put(2)
        print('跳过')
        return 2
    elif tup==(9, 39, 64, 255) or tup==(9, 40, 65, 255):
        q.put(3)
        print('胜利')
        return 3
    elif tup==(28, 28, 43, 255):
        q.put(4)
        print('关卡奖励')
        return 4
    else:
        q.put(0)
        print('其他')
        return 0

def get_statement1(q):
    get_pic('risk')
    im=cv2.imread('risk.png',0)
    try:
        dot=im[72,1840]
    except:
        print('不是横屏')
    print(dot)
    if dot==30:
        q.put(1)
        print('闯关')
        return 1
    elif dot>=110:
        q.put(2)
        print('跳过')
        return 2
    elif dot==32:
        q.put(3)
        print('胜利')
        return 3
    elif dot==29:
        q.put(4)
        print('关卡奖励')
        return 4
    else:
        q.put(0)
        print('其他')
        return 0


def get_state(q):
    while 1:
        get_statement(q)
#        time.sleep(0.2)

def press_where(statement):
    if statement==0:
        pass
    elif statement==1:
        random_tap(1370,870,1580,957)
    elif statement==2:
        random_tap(1850,87,1900,100)
    elif statement==3:
        random_tap(1516,937,1644,1000)
    elif statement==4:
        random_tap(1516,937,1644,1000)

def press_w(q):
    while 1:
        statement=q.get(True)
        press_where(statement)
        #time.sleep(0.7)

def main():
    q=Queue()
    pg=Process(target=get_state,args=(q,))
    pp=Process(target=press_w,args=(q,))
    pg.start()
    pp.start()
    pg.join()
    pp.terminate()
    
if __name__=='__main__':
    main()