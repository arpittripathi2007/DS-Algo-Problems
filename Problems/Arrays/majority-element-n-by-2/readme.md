

# Problem Statement
===================

Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

Example 1:

Input: nums = [3,2,3]
Output: 3


# URL
================

https://leetcode.com/problems/majority-element/

# CODE
================
```
def majorityElement(nums) -> int:
    count = 0
    candidate = 0
    for item in nums:
        if(count == 0):
            candidate = item
        if(candidate == item):
            count += 1
        else:
            count -= 1
    return candidate
```