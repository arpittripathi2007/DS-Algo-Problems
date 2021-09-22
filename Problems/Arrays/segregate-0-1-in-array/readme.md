

# Problem Statement
===================

You are given an array of 0s and 1s in random order. Segregate 0s on left side and 1s on right side of the array [Basically you have to sort the array]. Traverse array only once. 

Input array   =  [0, 1, 0, 1, 0, 0, 1, 1, 1, 0] 
Output array =  [0, 0, 0, 0, 0, 1, 1, 1, 1, 1] 

# URL
================

https://www.geeksforgeeks.org/segregate-0s-and-1s-in-an-array-by-traversing-array-once/

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