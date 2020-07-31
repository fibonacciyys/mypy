# -*- coding: utf-8 -*-
"""
Created on Mon Jul 13 11:50:00 2020

@author: ReoNa
"""
import collections

class Solution(object):
    def __init__(self):
        self.nums1 = [1,2,4,5,5]
        self.nums2 = [2,55,6,5,5,5]
        
    def intersect(self, nums1, nums2):
        if len(nums1) > len(nums2):
            return self.intersect(nums2,nums1)
        res = []
        c = collections.Counter(nums1)
        for num in nums2:
            if c.get(num,0) > 0:
                c[num] -= 1
                res.append(num)
                if c[num] == 0:
                    del c[num]
        return res
    
if __name__ == '__main__':
    solution = Solution()
    res = solution.intersect(solution.nums1,solution.nums2)
    print(res)