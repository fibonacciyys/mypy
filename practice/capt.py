# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 14:13:29 2020

@author: ReoNa
"""

from captcha.image import ImageCaptcha
from random import randint
list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
    '', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
chars = ''
for i in range(4):
  chars += list[randint(0, 61)]
image = ImageCaptcha().generate_image(chars)
 
image.show()