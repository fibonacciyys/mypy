# -*- coding: utf-8 -*-
"""
Created on Fri Jan 10 17:29:05 2020

@author: ReoNa
"""
import numpy as np

def check_zero(mat):
    for line in mat:
        for value in line:
            if value == '0':
                return True 

def maximalSquare(matrix) -> int:
    max_mal = 0
    if matrix == [] or matrix == [[]] or matrix == [['0']]:
        return max_mal
    elif matrix == [['1']]:
        max_mal = 1
    else:
        mat = np.array(matrix)
        l_l = len(matrix)
        r_l = len(matrix[0])
        l = min(l_l,r_l)
        for i in range(l):
            for j in range(len(matrix) - i):
                for k in range(len(matrix[0]) - i):
                    mat_test = mat[j:j+i+1,k:k+i+1]
                    if check_zero(mat_test):
                        pass
                    else:
                        max_mal = max((i+1)*(i+1),max_mal)
    return max_mal
                    
def maximalSquare2(matrix):
    if matrix == []:
            return 0
    max_l = 0
    matrix = np.array(matrix,dtype = np.int)
    mat = np.zeros(matrix.shape,dtype = np.int)
    x,y = matrix.shape
    for i in range(x):
        for j in range(y):
            if matrix[i,j] == 1:
                ij = min(mat[i-1,j-1],mat[i-1,j],mat[i,j-1]) + 1
                mat[i,j] = ij
                max_l = max(max_l,ij)
    return max_l*max_l
                

re = maximalSquare2([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]])
print(re)
re = maximalSquare2([['0','1']])
print(re)
        
        