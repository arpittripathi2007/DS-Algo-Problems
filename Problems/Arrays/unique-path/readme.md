

# Problem Statement (HARD || RECURSION || DP || COMBINATION): GOOGLE
===================

A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?

Example 1:
Input: m = 3, n = 7
Output: 28

Example 2:
Input: m = 3, n = 2
Output: 3
Explanation:
From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Down -> Down
2. Down -> Down -> Right
3. Down -> Right -> Down

# URL
================

https://leetcode.com/problems/unique-paths/

Solution: https://www.youtube.com/watch?v=t_f0nwwdg5o&list=PLgUwDviBIf0rPG3Ictpu74YWBQ1CaBkm2&index=18

# CODE
================

```
def uniquePaths(m: int, n: int) -> int:
    N = n + m -2
    r = m - 1
    res = 1
    
    for i in range(1, r+1):
        res *= (N-r + i)/i
    return int(round(res))
```