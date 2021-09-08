

# Problem Statement
===================

Given an integer array nums that may contain duplicates, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

 

Example 1:

Input: nums = [1,2,2]
Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]

# URL
================

https://leetcode.com/problems/subsets-ii/

# CODE
================
```
def find_subset(index, nums, ds, ans_):
    ans_.append(list(ds))
    for i in range(index, len(nums)):
      if(i != index and nums[i]==nums[i-1]):
        continue
      ds.append(nums[i])
      find_subset(i+1, nums, ds, ans_)
      ds.pop()
        
  def subsetsWithDup(self, nums):
    ds = []
    ans_ = []
    nums.sort()
    find_subset(0, nums,ds, ans_)
    return ans_
```