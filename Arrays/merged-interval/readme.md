

# Problem Statement
===================

Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

 

Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].


# URL
================

https://leetcode.com/problems/merge-intervals/


# CODE
================
```

def merge(intervals: List[List[int]]) -> List[List[int]]:
    intervals.sort()
    temp_interval = intervals[0]
    res_interval = []

    for item in intervals:
        if item[0] <= temp_interval[1]:
            temp_interval[1] = max(temp_interval[1], item[1])
        else:
            res_interval.append(temp_interval)
            temp_interval = item
    res_interval.append(temp_interval)   
    return res_interval

```