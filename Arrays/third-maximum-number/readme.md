

# Problem Statement
===================

Given integer array nums, return the third maximum number in this array. If the third maximum does not exist, return the maximum number.

 

Example 1:

Input: nums = [3,2,1]
Output: 1
Explanation: The third maximum is 1.


# URL
================

https://leetcode.com/problems/third-maximum-number/

# CODE
================

```
def thirdMax(self, nums: List[int]) -> int:
    s=sorted(list(set(nums)))
    return (s[-1] if len(s)<3 else s[-3])
```