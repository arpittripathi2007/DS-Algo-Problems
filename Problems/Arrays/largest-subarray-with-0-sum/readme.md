

# Problem Statement
===================

Given an array having both positive and negative integers. The task is to compute the length of the largest subarray with sum 0.

Example 1:

Input:
N = 8
A[] = {15,-2,2,-8,1,7,10,23}
Output: 5
Explanation: The largest subarray with
sum 0 will be -2 2 -8 1 7.
Your Task:
You just have to complete the function maxLen() which takes two arguments an array A and n, where n is the size of the array A and returns the length of the largest subarray with 0 sum.

Expected Time Complexity: O(N).

# URL
================

https://practice.geeksforgeeks.org/problems/largest-subarray-with-0-sum/1#

# CODE
================

```
def maxLen(n, arr):
    seen_values = {}
    max_length = 0
    sum_values = 0
    for i in range(n):
        sum_values += arr[i]
        if sum_values == 0:
            max_length = max(max_length, i+1)
        elif sum_values in seen_values:
            max_length = max(max_length, i - seen_values[sum_values])
        else:
            seen_values[sum_values] = i
    return max_length
```