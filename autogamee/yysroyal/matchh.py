# -*- coding: utf-8 -*-
"""
Created on Fri May 17 00:37:16 2019

@author: YY
"""

import cv2
import numpy as np

def mathc_img(image,Target,value):
    img_rgb = cv2.imread(image)
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    template = cv2.imread(Target,0)
    w, h = template.shape[::-1]
    res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
    threshold = value
    loc = np.where( res >= threshold)
    for pt in zip(*loc[::-1]):
        cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (7,249,151), 2)   
    cv2.imshow('Detected',img_rgb)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
def get_position(image,Target,value):
    img_rgb = cv2.imread(image)
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    template = cv2.imread(Target,0)
    w, h = template.shape[::-1]
    res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
    threshold = value
    loc = np.where( res >= threshold)
    xy_loc = list(zip(*loc[::-1]))
    center_loc = []
    for i in xy_loc:
        center_loc.append((i[0]+int(w/2),i[1]+int(h/2)))
    return center_loc

def test_para(image,Target,value):
    xy = get_position(image,Target,value)
    print(xy)
    mathc_img(image,Target,value)
    
if __name__ == '__main__':
    test_para(r'pics\bottom_full.png',r'pics\full.png',0.7)
#    test_para(r'test.png',r'pics\all.png',0.8)
    
    
    
    
    
    
