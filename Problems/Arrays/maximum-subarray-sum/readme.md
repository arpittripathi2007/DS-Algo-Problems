

# Problem Statement
===================

Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

 

Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.


# URL
================

https://leetcode.com/problems/maximum-subarray/submissions/

# CODE
================
```

def maxSubArray(nums):
    maxSum = nums[0]
    sum_ = 0
    
    for item in nums:
        sum_ += item
        if maxSum < sum_:
            maxSum = sum_
        sum_ = 0 if sum_ < 0 else sum_
        
    return maxSum

```