# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 09:56:51 2020

@author: ReoNa
"""

class Solution:
    def __init__(self):
        self.triangle = [
             [2],
            [3,4],
           [6,5,7],
          [4,1,8,3]]
        
    def minimumTotal(self,triangle):
        def add_big(li):
            li.append(10**8)
            li.insert(0,10**8)
            return li
            
        dp = list(map(add_big,triangle))
        n = len(dp)
        for j in range(1,n):
            for i in range(1,j+2):
                dp[j][i] = dp[j][i] + min(dp[j-1][i],dp[j-1][i-1])
        return min(dp[-1])

if __name__ == '__main__':
    solution = Solution()
    minimum = solution.minimumTotal(solution.triangle)
    print(minimum)