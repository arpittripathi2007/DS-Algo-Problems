

# Problem Statement
===================

Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.

Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true

# URL
================

https://leetcode.com/problems/search-a-2d-matrix/

# CODE
================
```
def searchMatrix(matrix: List[List[int]], target: int) -> bool:
    if(len(matrix) == 0):
        return False
    
    
    m = len(matrix)
    n = len(matrix[0])
    
    low = 0
    high = (m * n) -1
    
    while(low<=high):
        mid = (low + (high - low) // 2)
        
        if(matrix[mid//m][mid % m] == target):
            return True
        
        elif(matrix[mid//m][mid % m] < target):
            low = mid + 1
        else:
            high = mid - 1
            
    return False
```