

# Problem Statement
===================

Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

0 <= a, b, c, d < n
a, b, c, and d are distinct.
nums[a] + nums[b] + nums[c] + nums[d] == target
You may return the answer in any order.

 

Example 1:

Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
Example 2:

Input: nums = [2,2,2,2,2], target = 8
Output: [[2,2,2,2]]

# URL
================

https://leetcode.com/problems/4sum/

# CODE
================

```
def fourSum(nums: List[int], target: int) -> List[List[int]]:
    nums.sort()

    if len(nums) < 4:
        return []

    else:

        temp = set()

        for i in range(len(nums) - 3):
            for j in range(i + 1, len(nums) - 2):

                p = j + 1
                q = len(nums) - 1

                while p < q:

                    if (nums[i] + nums[j]) == target - (nums[p] + nums[q]):

                        temp.add((nums[i], nums[j], nums[p], nums[q]))
                        p += 1
                        q -= 1

                    elif (nums[i] + nums[j]) > target - (nums[p] + nums[q]):
                        q -= 1

                    else:
                        p += 1

        return (temp)
```