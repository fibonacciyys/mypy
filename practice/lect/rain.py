# -*- coding: utf-8 -*-
"""
Created on Wed Jan  8 00:15:50 2020

@author: ReoNa
"""

import matplotlib.pyplot as plt
import numpy as np

class Rain(object):
    def __init__(self,li):
        self.li = li
        self.rain_sum = 0
        self.head_zero = 0
        self.tail_zero = 0
        self.graph = []
        self.data = []
    
    def trim_zero(self):
        try:
            while self.li[0] == 0:
                self.li.pop(0)
                self.head_zero += 1
            while self.li[-1] == 0:
                self.li.pop(-1)
                self.tail_zero += 1
            self.graph.append(
                    [' '] * self.head_zero + list(map(lambda x:str(x),self.li)) + [' '] * self.tail_zero)
            self.data.append(
                    [-1] * self.head_zero + list(np.sign(self.li)) + [-1] * self.tail_zero)
        except:
            self.li = []
        
    def count_zero(self):
        zero_num = 0
        if not len(self.li) == 0:
            for i in self.li:
                if i == 0:
                    zero_num += 1
            return zero_num
        else:
            return 0
    
    def select_reduce_one(self,x):
        return x if x == 0 else x-1
    
    def reduce_one(self):
        self.li = [self.select_reduce_one(x) for x in self.li]
    
    def get_rain(self):
        print('num_list:',self.li)
        while not len(self.li) < 3:
            self.trim_zero()
            self.rain_sum += self.count_zero()
            self.reduce_one()
        print('rain_sum:',rain1.rain_sum)
#        self.num_list_print()
        self.draw()
    
    def num_list_print(self):
        for i in  self.graph[::-1]:
            print(i)
    
    def draw(self):
        fig, ax = plt.subplots()
        ax.pcolor(self.data, cmap=plt.cm.Blues)
        plt.show()
        
if __name__ == '__main__':
    rain1 = Rain([1,4,2,7,9,0,2,4,8,0,3,16,0,7,3,1,17,0,4,9,2,1,5])
    rain1.get_rain()
    