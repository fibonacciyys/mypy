# -*- coding: utf-8 -*-
"""
Created on Fri May 17 23:12:21 2019

@author: YY
"""

import win32gui
import win32ui
import win32con
from ctypes import windll
from PIL import Image
import os,radd
import cv2
import numpy as np

def screencap(name):
    hwnd=win32gui.FindWindow(None,name + ' (仅限非商业用途)')
#    print(hwnd)
#    hwndChildList = []     
#    win32gui.EnumChildWindows(hwnd, lambda hwnd, param: param.append(hwnd),  hwndChildList)          
#    print(hwndChildList)
#    hwnd=hwndChildList[0]
#    print(hwnd)
    # 获取窗口位置
    left, top, right, bot = win32gui.GetWindowRect(hwnd)
    #获取某个句柄的类名和标题
    
    #print(left,top,right,bot)
    #window_capture(handle,'test.jpg')
    w = right - left
    h = bot - top
    
    # 返回句柄窗口的设备环境、覆盖整个窗口，包括非客户区，标题栏，菜单，边框
    hwndDC = win32gui.GetWindowDC(hwnd)
    
    # 创建设备描述表
    mfcDC  = win32ui.CreateDCFromHandle(hwndDC)
    
    # 创建内存设备描述表
    saveDC = mfcDC.CreateCompatibleDC()
    
    # 创建位图对象
    saveBitMap = win32ui.CreateBitmap()
    saveBitMap.CreateCompatibleBitmap(mfcDC, w, h)
    saveDC.SelectObject(saveBitMap)
    
    # 截图至内存设备描述表
    img_dc = mfcDC
    mem_dc = saveDC
    mem_dc.BitBlt((0, 0), (w, h), img_dc, (0, 0), win32con.SRCCOPY)
    # 将截图保存到文件中
#    saveBitMap.SaveBitmapFile(mem_dc, 'screenshot.bmp')
    
    # 改变下行决定是否截图整个窗口，可以自己测试下
    result = windll.user32.PrintWindow(hwnd, saveDC.GetSafeHdc(), 1)
#    result = windll.user32.PrintWindow(hwnd, saveDC.GetSafeHdc(), 0)
#    print(result)
    
    # 获取位图信息
    bmpinfo = saveBitMap.GetInfo()
    bmpstr = saveBitMap.GetBitmapBits(True)
    # 生成图像
    im = Image.frombuffer(
        'RGB',
        (bmpinfo['bmWidth'], bmpinfo['bmHeight']),
        bmpstr, 'raw', 'BGRX', 0, 1)
    
    # 内存释放
    win32gui.DeleteObject(saveBitMap.GetHandle())
    saveDC.DeleteDC()
    mfcDC.DeleteDC()
    win32gui.ReleaseDC(hwnd, hwndDC)
    
    # 存储截图
    if result == 1:
        #PrintWindow Succeeded
        im.save("test.png")
    #    im.show()
    
def open_pic_grey(Target):
    template = cv2.imread(Target,0)
    return template

def get_position(image,Target,value):
    img_rgb = cv2.imread(image)
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    w, h = Target.shape[::-1]
    res = cv2.matchTemplate(img_gray,Target,cv2.TM_CCOEFF_NORMED)
    threshold = value
    loc = np.where( res >= threshold)
    xy_loc = list(zip(*loc[::-1]))
    center_loc = []
    for i in xy_loc:
        center_loc.append((i[0]+int(w/2),i[1]+int(h/2)))
    return center_loc

def get_pic(pic_name):
    os.system('adb shell screencap -p  /sdcard/'+pic_name+'.png')
    os.system('adb pull /sdcard/'+pic_name+'.png')
    
def swipee(x1,y1,x2,y2):
    os.system('adb shell input swipe '+str(x1)+' '+str(y1)+' '+str(x2)+' '+str(y2))

def point_biase(x,y,biase=5):
    return radd.get_point(x-biase,y-biase,x+biase,y+biase)

def swipe_biase(x1,y1,x2,y2,biase=5):
    x3,y3 = point_biase(x1,y1)
    x4,y4 = point_biase(x2,y2)
    swipee(x3,y3,x4,y4)
    
def tapp(x1,y1):
    os.system('adb shell input tap '+str(x1)+' '+str(y1))
    
def sw_or_tap(x1,y1,x2,y2):
    x3,y3=radd.get_point(x1,y1,x2,y2)
    x4,y4=radd.get_point(x1,y1,x2,y2)
    if radd.get_o_l()==1:
        swipee(x3,y3,x4,y4)
    else:
        tapp(x3,y3)
        
def random_tap(x1,y1,x2,y2):
    x3,y3=radd.get_point(x1,y1,x2,y2)
    tapp(x3,y3)
    
def tap_biase(loc,biase):
    x,y = loc
    random_tap(x-biase,y-biase,x+biase,y+biase)