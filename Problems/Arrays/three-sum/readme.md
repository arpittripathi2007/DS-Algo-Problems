

# Problem Statement
===================

Given an array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number.

Return the indices of the two numbers (1-indexed) as an integer array answer of size 2, where 1 <= answer[0] < answer[1] <= numbers.length.

The tests are generated such that there is exactly one solution. You may not use the same element twice.

 

Example 1:

Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.

# URL
================

https://leetcode.com/problems/3sum/

# CODE
================

```
def threeSum(nums):
    res = []
    nums.sort()
    for i, num in enumerate(nums):
        if i>0 and num == nums[i-1]:
            continue
        left = i +1 
        end = len(nums)-1
        
        while left < end:
            three_sums = num + nums[left] + nums[end]
            
            if three_sums < 0:
                left += 1
            elif three_sums > 0:
                end -= 1
            else:
                res.append([num, nums[left], nums[end]])
                left += 1
                while(nums[left] == nums[left-1] and left < end):
                    left += 1
    return res
```