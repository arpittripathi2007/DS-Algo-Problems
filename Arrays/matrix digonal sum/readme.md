

# Problem Statement
===================

Given a square matrix mat, return the sum of the matrix diagonals.

Only include the sum of all the elements on the primary diagonal and all the elements on the secondary diagonal that are not part of the primary diagonal.

Input: mat = [[1,2,3],
              [4,5,6],
              [7,8,9]]
Output: 25
Explanation: Diagonals sum: 1 + 5 + 9 + 3 + 7 = 25
Notice that element mat[1][1] = 5 is counted only once.
 


# URL
================

https://leetcode.com/problems/matrix-diagonal-sum/

# CODE
================
```
def diagonalSum(self, mat: List[List[int]]) -> int:
    len_ = len(mat)
    sum_ = 0
    
    for i in range(len_):
        sum_ += mat[i][i]
    
    j = len_ - 1
    for i in range(len_):
        sum_ += mat[i][j]
        j -= 1
    if len_%2 != 0:
        sum_ -= mat[len_//2][len_//2]
    return sum_
```