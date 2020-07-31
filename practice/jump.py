# -*- coding: utf-8 -*-
"""
Created on Wed Jan  8 22:44:46 2020

@author: ReoNa
"""

class Jump(object):
    def __init__(self,li):
        self.li = li
            
    def jump_Li(self):
        max_num = 0
        for (ind,value) in enumerate(self.li):
            max_num = max(value,max_num-1)
            if (max_num == 0) and (ind != len(self.li)-1):
                return False
        return True
           
        
if __name__ == '__main__':
    jump1 = Jump([3,2,1,0,4])
    print(jump1.jump_Li())