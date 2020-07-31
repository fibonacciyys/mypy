#!C:\Anaconda3\python
import time
from interactt import sw_or_tap,get_pic
from multiprocessing import Process,Queue
from PIL import Image
#im1=Image.open('ten_end.png')
#im0=Image.open('ten_start.png')
#print(im0.getpixel((880,790)))
#print(im1.getpixel((880,790)))
#os.system('adb devices')
    
def press_start():
    x1,y1=1350,710
    x2,y2=1520,780
    sw_or_tap(x1,y1,x2,y2)
    
def press_end():
    x1,y1=850,880
    x2,y2=1110,1040
    sw_or_tap(x1,y1,x2,y2)

def select():
    get_pic('yys')
    im=Image.open('yys.jpg')
    pixx=im.load()
    tup=pixx[880,790]
    print(tup)
    if tup==(163,97,39,255):
        press_start()
        print('start ten')
        return 40
    elif tup==(123,175,221,255):
        press_end()
        print('end ten')
        return 2
    else:
        return 0.001
    im.close()
        
def main1():
    timee=0
    while 1:
        xx=select()
        if xx==0.001:
            timee+=1
        else:
            timee=0
        if timee>13:
            sw_or_tap(1245,760,1321,802)
            timee=0  #1283,781,1245,760
        time.sleep(xx)

def get_statement(q):
    get_pic('yys')
    im=Image.open('yys.jpg')
    pixx=im.load()
    tup=pixx[880,790]
    print(tup)
    if tup==(163,97,39,255):
        q.put(1)
        return 1
    elif tup==(123,175,221,255):
        q.put(2)
        return 2
    elif tup==(48, 28, 34, 255):
        pass
    else:
        q.put(3)
        return 3

def get_state(q):
    while 1:
        get_statement(q)
        

def press_ten(statement):
    if statement==1:
        press_start()
    if statement==2:
        press_end()
    if statement==3:
        #sw_or_tap(1245,760,1321,802)
        pass

def press_t(q):
    while 1:
        statement=q.get(True)
        press_ten(statement)
        del statement


def main2():
    q=Queue()
    pg=Process(target=get_state,args=(q,))
    pp=Process(target=press_t,args=(q,))
    pg.start()
    pp.start()
    pg.join()
    pp.terminate()

if __name__=='__main__':
    main1()