

# Problem Statement
===================

Given a binary array nums, return the maximum number of consecutive 1's in the array.
Example 1:

Input: nums = [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.


# URL
================

https://leetcode.com/problems/max-consecutive-ones/

# CODE
================

```
def findMaxConsecutiveOnes(nums: List[int]) -> int:
    count = 0
    max_count = 0
    
    for item in nums:
        if item == 1:
            count += 1
        else:
            max_count = max(max_count, count)
            count = 0
    max_count = max(max_count, count)
    return max_count
```