# -*- coding: utf-8 -*-
"""
Created on Tue Feb 19 20:47:17 2019

@author: YY
"""

import win32gui
import win32con
import win32ui
import ctypes
from PIL import Image

def main():
    ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")
    length = len(ascii_char)
    def convert(img):
        img = img.convert("L")  # 转为灰度图像
        txt = ""
        for i in range(img.size[1]):
            for j in range(img.size[0]):
                gray = img.getpixel((j, i))     # 获取每个坐标像素点的灰度
                unit = 256.0 / length
                txt += ascii_char[int(gray / unit)] #获取对应坐标的字符值
            txt += '\n'
        return  txt
#    dll1 = ctypes.windll.LoadLibrary(r'C:\Users\李协钊\source\repos\Dll1\Debug\Dll1.dll')
    dll2 = ctypes.CDLL(r'C:\Users\李协钊\source\repos\Dll1\x64\Debug\Dll1.dll')
    dll2.HideCursor()
    hwnd=win32gui.FindWindow('SE_SogouExplorerFrame',None)
    #,'百度一下，你就知道 - 狠愛雪丶情殇的浏览器'
#    clsname = win32gui.GetClassName(hwnd)
    while True:
#        os.system('cls')
        dll2.gotoxy(0,0)
#        time.sleep(0.5)
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
#        im.save("test.png")
        
        (width,height) = im.size
        prop=0.2
        im = im.resize((int(width*0.4*prop),int(height*0.21*prop)))
        txt = convert(im)
        print(txt)
    #    print(clsname)
    
if __name__ == '__main__':
    main()