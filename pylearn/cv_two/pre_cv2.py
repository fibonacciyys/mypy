# -*- coding: utf-8 -*-
"""
Created on Mon Jul  2 20:38:48 2018

@author: YY
"""

import cv2 as cv

im=cv.imread('yys.jpg')
print(im[100,100])
cv.namedWindow("Image")
cv.imshow("Image",im)
cv.waitKey(0)
del im
cv.destroyAllWindows()