# -*- coding: utf-8 -*-
"""
Created on Sat May 18 12:39:40 2019

projection:865,550
prototype:1920,1080

@author: YY
"""
import screenn
import time
import sys
#import ctypes
import os

class YYS_script(object):
    def __init__(self,name,dungeon,state=0,orchin=0,bossfound=0,error=0,exchanging=0,targets={}):
        self.name = name
        self.dungeon = dungeon
        self.state = state
        self.orchin = orchin
        self.bossfound = bossfound
        self.error = 0
        self.exchanging = exchanging
        self.targets = targets
        
    def load_pics(self):
        if self.dungeon == 1:
            target_list = ['boss','box','chapter28','enter','config','src','all','full',
                       'exit','explore','fight','ready','reward','cover','message']
            for target in target_list:
                self.targets[target] = screenn.open_pic_grey('pics\\' + target + '.png')
        elif self.dungeon == 2:
            target_list = ['start','ready','reward','cover','config','message']
            for target in target_list:
                self.targets[target] = screenn.open_pic_grey('pics\\' + target + '.png')
        else:
            pass
    
    def scale_xy(self,pos):
        x,y = pos
        x,y = x*2.22,(y-63)*2.22
        return (int(x),int(y))
    
    def swipe_biase(self,x1,y1,x2,y2,biase=10):
        x1,y1 = self.scale_xy((x1,y1))
        x2,y2 = self.scale_xy((x2,y2))
        screenn.swipe_biase(x1,y1,x2,y2,biase)
    
    def next_state(self,pos_li,change=1,biase=5):
        xy = pos_li[0]
        xy = self.scale_xy(xy)
        print(xy)
        screenn.tap_biase(xy,biase)
        self.state += change
        self.error = 0
        
    def next_orchin(self,pos_li,biase=5):
        xy = pos_li[0]
        xy = self.scale_xy(xy)
        print(xy)
        screenn.tap_biase(xy,biase)
        self.state += 1
        self.orchin += 1
        
    def get_pos(self,target,threshold=0.8):
        return screenn.get_position('test.png',self.targets[target],threshold)
    
    def check_exist(self,target='cover',threshold=0.8):
        return len(self.get_pos(target,threshold)) != 0
    
    def down_two(self,pos):
        x,y = pos
        return x-320+y-282 > -10
    
    def check_full(self):
        if self.check_exist('full',0.7):
            pos_li = self.get_pos('full',0.7)
            for i in pos_li:
                if self.down_two(i):
                    self.exchanging = 1
                    break
    
    def exchange(self):
        if self.state < 2.1:
            self.next_state([(324,424)],0,10)
            self.next_state([(324,424)],0,10)
            self.state += 0.2
        elif self.state < 2.3:
            try:
                pos_li = self.get_pos('all')
                self.next_state(pos_li,0,2)
                self.state += 0.2
                time.sleep(0.7)
            except:
                pass
        elif self.state < 2.5:
            try:
                pos_li = self.get_pos('src')
                self.next_state(pos_li,0,2)
                self.state += 0.2
            except:
                pass
        elif self.state < 2.7:
            self.swipe_biase(405,455,415,315)
            time.sleep(0.1)
            self.swipe_biase(490,455,130,280)
            time.sleep(0.1)
            self.next_state([(780,430)],0.5)
            self.state = int(self.state)
            self.exchanging = 0
        else:
            pass
    
    def print_info(self):
        pri_li = ['state','error','bossfound','orchin','exchanging']
        for i in pri_li:
            exec("print('" + i + ":',self." + i + ",end='  ')")
        print()
    
    def searching(self):
        os.system('cls')
#        try:
#            dll1 = ctypes.CDLL(os.getcwd() + '\\Dll1\\x64\\Debug\\Dll1.dll')
#            dll1.HideCursor()
#        except:
#            pass
        while True:
#            try:
#                dll1.gotoxy(0,0)
#            except:
#                pass
            self.print_info()
            screenn.screencap(self.name)
            if self.state < 1:
                self.bossfound = 0
                pos_li = self.get_pos('explore')
                try:
                    self.next_state(pos_li)
                except:
                    if self.check_exist('chapter28',0.9):
                        pos_li = self.get_pos('chapter28',0.9)
                        self.next_state(pos_li,0)
                    elif  self.check_exist():
                        pass
                    elif self.check_exist('exit'):
                        self.error += 1
                    else:
                        self.state += 1
                    if self.error > 10:
                        self.error = 0
                        self.state += 1
            elif self.state < 2:
                if self.orchin < 3:
                    pos_li = self.get_pos('fight',0.6)
                    try:
                        self.next_orchin(pos_li)
                    except:
                        if self.check_exist():
                            pass
                        elif self.check_exist('exit'):
                            screenn.swipe_biase(1280,540,640,540)
                            time.sleep(0.6)
                            self.error += 1
                        else:
                            self.state += 1
                        if self.error > 5:
                            self.error = 0
                            self.state += 1
                else:
                    pos_li = self.get_pos('boss')
                    try:
                        self.next_state(pos_li)
                        self.bossfound = 1
                        self.orchin = 0
                    except:
                        if self.check_exist():
                            pass
                        else:
                            pos_li = self.get_pos('fight',0.6)
                            try:
                                self.next_orchin(pos_li,biase=0)
                            except:
                                screenn.swipe_biase(1280,540,640,540)
                                time.sleep(1)
                                self.error += 1
                                if self.error > 5:
                                    self.error = 0
                                    self.state += 1
            elif self.state < 3:
                self.check_full()
                if self.exchanging:
                    self.exchange()
                elif self.check_exist('config'):
                    try:
                        time.sleep(0.05)
                        pos_li = self.get_pos('ready')
                        self.next_state(pos_li)
                    except:
                        pass
                else:
                    if self.check_exist():
                        pass
                    elif self.check_exist('message'):
                        pass
                    else:
                        self.error +=1 
                    if self.error >7:
                        self.error = 0
                        self.state += 1
            elif self.state < 4:
                pos_li = self.get_pos('reward')
                try:
                    if not self.bossfound:
                        if self.check_exist() or self.check_exist('exit',0.95):
                            self.state -= 2
                        self.next_state(pos_li,0)
                    else:
                        if self.check_exist() or self.check_exist('exit',0.95):
                            self.state += 1
                        self.next_state(pos_li,0)
                except:
                    if self.check_exist('message'):
                        pass
                    else:
                        self.error += 1
                if self.error > 50:
                    self.error = 0
                    self.state += 1
            elif self.state < 5:
                if self.check_exist('box'):
                    pos_li = self.get_pos('exit')
                    self.next_state(pos_li,0)
                    time.sleep(0.5)
                    try:
                        pos_li = self.get_pos('enter')
                        self.next_state(pos_li)
                        self.state = 0
                    except:
                        self.error += 1
                    if self.error > 13:
                        self.error = 0
                        self.state = 0
                elif self.check_exist():
                    pass
                elif self.check_exist('enter'):
                    pos_li = self.get_pos('enter')
                    self.next_state(pos_li)
                    self.state = 0
                elif self.check_exist('exit'):
                    self.error += 1
                else:
                    self.state = 0
                if self.error > 19:
                    self.error = 0
                    self.state = 0
            else:
                pass
            
    def search_ten(self):
        os.system('cls')
        while True:
            screenn.screencap('test')
            if self.state < 1:
                try:
                    pos_li = self.get_pos('start')
                    self.next_state(pos_li)
                except:
                    if self.check_exist():
                        pass
                    else:
                        self.error += 1
                if self.error > 10:
                    self.error = 0
                    self.state += 1
            elif self.state < 2:
                if self.check_exist():
                    pass
                elif self.check_exist('config'):
                    time.sleep(0.5)
                    pos_li = self.get_pos('ready')
                    self.next_state(pos_li)
                    for i in range(20):
                        print(i,'second')
                        time.sleep(1)
                else:
                    self.error += 1
                if self.error > 10:
                    self.error = 0
                    self.state += 1
            elif self.state < 3:
                if self.check_exist('message'):
                    pass
                elif self.check_exist('reward'):
                    pos_li = self.get_pos('reward')
                    self.next_state(pos_li)
                else:
                    self.error += 1
                if self.error > 50:
                    self.error = 0
                    self.state = 0
            else:
                pass


def test():
    scr1 = YYS_script('Xiaomi-MI MAX',1)
    scr1.load_pics()
    print(dir(scr1))
    exec('print(scr1.error)')
#    cv2.imshow('boss',scr1.targets['boss'])
#    cv2.waitKey(0)
#    cv2.destroyAllWindows()
    
def test_searching():
    try:
        mode = int(sys.argv[1])
        orchin = 3*int(sys.argv[2])
    except:
        mode = 1
        orchin = 0
    scr1 = YYS_script('Xiaomi-MI MAX',mode,orchin=orchin)
    scr1.load_pics()
    scr1.searching()
    
if __name__ == '__main__':    
    test_searching()
#    test()