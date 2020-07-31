# -*- coding: utf-8 -*-
"""
Created on Sun Jul 12 20:06:07 2020

@author: ReoNa
"""

class Solution:
    def __init__(self):
        self.dungeon = [[0,-2,3],
                        [-1,0,0],
                        [-3,-3,-2]]
        self.way = []
        self.dp = []
        self.m = 0
        self.n = 0
    
    def calculateMinimumHP(self,dungeon):
        m = len(dungeon[0])
        n = len(dungeon)
        self.m,self.n = m,n
        big_num = 10**8
        dp = [[big_num] * (m+1) for _ in range(n+1)]
        dp[n][m-1] = 1
        dp[n-1][m] = 1
        for i in range(n-1,-1,-1):
            for j in range(m-1,-1,-1):
                min_life = min(dp[i][j+1],dp[i+1][j])
#                self.way.append((i,j+1) if min_life == dp[i][j+1] else (i+1,j))
                dp[i][j] = max(min_life - dungeon[i][j],1)
        self.dp = dp
        return dp[0][0]
    
    def print_dp(self):
        for li in self.dp:
            print(li)
    
    def print_way(self):
        x,y = 0,0
        while x < self.m-1 or y < self.n-1:
            self.way.append((x,y))
            if self.dp[x+1][y] < self.dp[x][y+1]:
                x += 1
            else:
                y += 1
        self.way.append((self.m-1,self.n-1))  
        print('路径：',self.way)
    
    def print_dungeon(self):
        print('地下城：')
        for li in self.dungeon:
            print(li)
    
if __name__ == '__main__':
    solution = Solution()
    solution.print_dungeon()
    HP = solution.calculateMinimumHP(solution.dungeon)
    print('血量：',HP)
    solution.print_way()
    solution.print_dp()
    