

# Problem Statement
===================

Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's, and return the matrix.

You must do it in place.

Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]

# URL
================

https://leetcode.com/problems/set-matrix-zeroes/

# CODE
================
```
def setZeroes(matrix):
    """
    Do not return anything, modify matrix in-place instead.
    """
    rows = len(matrix)
    cols = len(matrix[0])
    
    col_0 = 1
    
    for i in range(rows):
        if(matrix[i][0]) == 0:
            col_0 = 0
        for j in range(1, cols):
            if(matrix[i][j] == 0):
                matrix[i][0] = matrix[0][j] = 0
    
    for i in range(rows-1, -1, -1):
        for j in range(cols-1, 0, -1):
            if(matrix[i][0] == 0 or matrix[0][j] == 0):
                matrix[i][j] = 0
        if col_0 == 0:
            matrix[i][0] = 0
    return matrix
```