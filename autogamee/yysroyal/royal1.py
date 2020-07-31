# -*- coding: utf-8 -*-
"""
Created on Sun Sep  9 14:38:46 2018

@author: YY
"""

import cv2
import interactt
import numpy as np
#import time
#from common import screenshot
import subprocess
from io import BytesIO
from PIL import Image

def test():
    img=cv2.imread('risk.png',0)
    cv2.imshow('init',img)
    cv2.waitKey(0)
    print(img[72,1840])
    temp=cv2.imread('again.png',0)
    res=cv2.matchTemplate(img,temp,cv2.TM_CCOEFF_NORMED)
    gps=[]
    loc=np.where(res>=0.99)
    sim_loc=zip(*loc[::-1])
    print(list(sim_loc)[0])
    #print(loc,*loc)
    for item in sim_loc:
        gps.append(item)
    #print(gps)
    
def main():
    while True:
        pixx=get_screen()
        try:
            dot=pixx.getpixel((1840,72))
        except:
            dot=-1
            print('不是横屏状态')
        print(dot)
        if dot==30:
            interactt.random_tap(1370,870,1580,957)
        elif dot>=110:
            interactt.random_tap(1850,87,1900,100)
        elif dot==32:
            interactt.random_tap(1516,937,1644,1000)
        elif dot==29:
            interactt.random_tap(1516,937,1644,1000)
        else:
            pass
#        time.sleep(0.3)
    
def get_screen():
    process = subprocess.Popen('adb shell screencap -p',shell=True, stdout=subprocess.PIPE)
    binary_screenshot = process.stdout.read()
    binary_screenshot = binary_screenshot.replace(b'\r\n', b'\n')
    im=Image.open(BytesIO(binary_screenshot)).convert('L')
    return im

def get_data():
    interactt.get_pic('risk')
    img_royal=cv2.imread('risk.png',0)
    dot=img_royal[72,1840]
    print(dot)
    
if __name__ == '__main__':
    main()