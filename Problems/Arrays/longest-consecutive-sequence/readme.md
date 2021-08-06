

# Problem Statement
===================

Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

 

Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

# URL
================

https://leetcode.com/problems/longest-consecutive-sequence/

# CODE
================

```
def longestConsecutive(nums: List[int]) -> int:
    stack_nums  = set()
    for item in nums:
        stack_nums.add(item)
    
    seen_count = 0
    max_seen_count = 0
    for item in stack_nums:
        if item in stack_nums:
            if item-1 in stack_nums:
                continue
            else:
                counter_item = item
                seen_count = 1
                while(counter_item+1 in stack_nums):
                    seen_count += 1
                    counter_item += 1
                max_seen_count = max(seen_count, max_seen_count)
                    
    return max_seen_count
```