# -*- coding: utf-8 -*-
"""
Created on Tue Sep 11 17:30:37 2018
-1 其他
0关卡胜利 (27,28,40) 653,484,123,39
1闯关 (19,30,39) 601,456,113,36   (18,34,53)
2跳过 (>230) 826,104,18,3
3三星 (9,40,67) 653,484,123,39
@author: YY
"""

import win32api
import win32gui
import win32con
import win32ui
from ctypes import windll
from PIL import Image
import random
import screenn
import time
import sys


def get_rad_bywh(x,y,w,h):
    x1=x+int(w*random.random())
    y1=y+int(h*random.random())
    return (x1,y1)

def abs_sum(pix,r,g,b):
    summ=0
    for (i1,i2) in zip(pix,(r,g,b)):
        summ+=abs(i1-i2)
    return summ

def pick_state(pix):
    summ=0
    for i in pix:
        summ+=i
    if summ>=720:
        return 2
    elif abs_sum(pix,27,28,40)<=5:
        return 0
    elif abs_sum(pix,19,30,39)<=5 or abs_sum(pix,18,34,53)<=5:
        return 1
    elif abs_sum(pix,9,40,67)<=5:
        return 3
    else:
        return -1

def tap(hwnd,x,y,w,h):
    tap_pos=get_rad_bywh(x,y,w,h)
    tmp=win32api.MAKELONG(tap_pos[0],tap_pos[1])
    win32gui.SendMessage(hwnd, win32con.WM_ACTIVATE,win32con.WA_ACTIVE,0)
    win32gui.SendMessage(hwnd, win32con.WM_LBUTTONDOWN,win32con.MK_LBUTTON,tmp)
    win32gui.SendMessage(hwnd, win32con.WM_LBUTTONUP,win32con.MK_LBUTTON,tmp)

def a_tap():
    win32api.SetCursorPos([30,150])
    #执行左单键击，若需要双击则延时几毫秒再点击一次即可
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP | win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)

def tapByState(hwnd,state):
    if state==2:
        tap(hwnd,826,104,18,3)
    elif state==0 or state==3:
        tap(hwnd,653,484,123,39)
    elif state==1:
        tap(hwnd,601,456,113,36)
        time.sleep(3)
    else:
        pass
        
def main():
    try:
        phone=sys.argv[1]
        if phone=='6':
            hwnd=win32gui.FindWindow(None,'Xiaomi-MI 6 (仅限非商业用途)')
        if phone=='max' or phone=='MAX':
            hwnd=win32gui.FindWindow(None,'Xiaomi-MI MAX (仅限非商业用途)')
    except:
        hwnd=win32gui.FindWindow(None,'Xiaomi-MI MAX (仅限非商业用途)')
    print(hwnd)
    while True:
        time.sleep(0.5)
        left, top, right, bot = win32gui.GetWindowRect(hwnd)
        w = right - left
        h = bot - top
        hwndDC = win32gui.GetWindowDC(hwnd)
        mfcDC  = win32ui.CreateDCFromHandle(hwndDC)
        saveDC = mfcDC.CreateCompatibleDC()
        saveBitMap = win32ui.CreateBitmap()
        saveBitMap.CreateCompatibleBitmap(mfcDC, w, h)
        saveDC.SelectObject(saveBitMap)
        img_dc = mfcDC
        mem_dc = saveDC
        mem_dc.BitBlt((0, 0), (w, h), img_dc, (0, 0), win32con.SRCCOPY)
        bmpinfo = saveBitMap.GetInfo()
        bmpstr = saveBitMap.GetBitmapBits(True)
        im = Image.frombuffer(
            'RGB',
            (bmpinfo['bmWidth'], bmpinfo['bmHeight']),
            bmpstr, 'raw', 'BGRX', 0, 1)
        win32gui.DeleteObject(saveBitMap.GetHandle())
        saveDC.DeleteDC()
        mfcDC.DeleteDC()
        win32gui.ReleaseDC(hwnd, hwndDC)
        try:
            pix=im.getpixel((814,89))
        except:
            pix=(-1,-1,-1)
            print('不是横屏状态')
        print(pix)
        state=pick_state(pix)
    #    tapByState(hwnd,state)
        if state==2:
            screenn.random_tap(1850,87,1900,100)
        elif state==0 or state==3:
            screenn.random_tap(1516,937,1644,1000)
        elif state==1:
            screenn.random_tap(1370,870,1580,957)
        else:
            pass
        
def screencap():
#    hwnd=win32gui.FindWindow(None,'Spyder (Python 3.6)')
#    hwnd=win32gui.FindWindow(None,'微信')
    
    hwnd=win32gui.FindWindow(None,'Xiaomi-MI MAX (仅限非商业用途)')
    print(hwnd)
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
    print(result)
    
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
#    pix=im.getpixel((814,89))
#    print(pix)
#    client_pos=(610,460)
#    handle= win32gui.WindowFromPoint(pos) 
# =============================================================================
#     client_pos =(610,460)
#     tmp=win32api.MAKELONG(client_pos[0],client_pos[1])
#     win32gui.SendMessage(hwnd, win32con.WM_ACTIVATE,win32con.WA_ACTIVE,0)
#     win32gui.SendMessage(hwnd, win32con.WM_LBUTTONDOWN,win32con.MK_LBUTTON,tmp)
#     win32gui.SendMessage(hwnd, win32con.WM_LBUTTONUP,win32con.MK_LBUTTON,tmp)
# =============================================================================
    
def test():
    hwnd=win32gui.FindWindow(None,'Xiaomi-MI MAX (仅限非商业用途)')
    title = win32gui.GetWindowText(hwnd)     
    clsname = win32gui.GetClassName(hwnd)
    left, top, right, bot = win32gui.GetWindowRect(hwnd)
    print(hwnd,title,clsname,left, top, right, bot)
    tap(hwnd,30,30,30,30)
    hwndChildList = []     
    win32gui.EnumChildWindows(hwnd, lambda hwnd, param: param.append(hwnd),  hwndChildList)          
    print(hwndChildList)
    for hwnd in hwndChildList:
        title = win32gui.GetWindowText(hwnd)     
        clsname = win32gui.GetClassName(hwnd)
        print(hwnd,title,clsname,left, top, right, bot)
        par=win32gui.GetParent(hwnd)
        title = win32gui.GetWindowText(par)     
        clsname = win32gui.GetClassName(par)
        print(par,title,clsname)
    tap(hwndChildList[0],30,30,30,30)
    par=win32gui.GetParent(hwnd)
    title = win32gui.GetWindowText(par)     
    clsname = win32gui.GetClassName(par)
    print(par,title,clsname)
    
def test1():
    hwnd=win32gui.FindWindow(None,'Total Control')
    title = win32gui.GetWindowText(hwnd)     
    clsname = win32gui.GetClassName(hwnd)
    left, top, right, bot = win32gui.GetWindowRect(hwnd)
    print(hwnd,title,clsname,left, top, right, bot)
    
def test_argv():
    try:
        phone=sys.argv[1]
        print(phone)
        if phone=='6':
            hwnd=win32gui.FindWindow(None,'Xiaomi-MI 6 (仅限非商业用途)')
        elif phone=='max' or phone=='MAX':
            hwnd=win32gui.FindWindow(None,'Xiaomi-MI MAX (仅限非商业用途)')
    except:
        hwnd=win32gui.FindWindow(None,'Xiaomi-MI MAX (仅限非商业用途)')
    print(hwnd)

    
if __name__ == '__main__':
#    main()
    screencap()