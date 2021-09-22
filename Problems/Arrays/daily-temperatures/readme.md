

# Problem Statement
===================

Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.

 

Example 1:

Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]
Example 2:

Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]

# URL
================

https://leetcode.com/problems/daily-temperatures/

# CODE
================

```
def dailyTemperatures(temperatures: List[int]) -> List[int]:
    stack = []
    
    res = [0 for i in range(len(temperatures))]
    
    for i in range(len(temperatures)):
        curr_ = temperatures[i]
        
        while stack and temperatures[stack[-1]] < curr_:
            less_index = stack.pop()
            res[less_index] = i - less_index
        stack.append(i)
    return res
```