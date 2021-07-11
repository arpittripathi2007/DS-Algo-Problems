

# Problem Statement
===================

Given two sorted arrays, we need to merge them in O((n+m)*log(n+m)) time with O(1) extra space into a sorted array, when n is the size of the first array, and m is the size of the second array.

Example:  

Input: ar1[] = {10};
       ar2[] = {2, 3};
Output: ar1[] = {2}
        ar2[] = {3, 10}  


# URL
================

https://www.geeksforgeeks.org/efficiently-merging-two-sorted-arrays-with-o1-extra-space/
(SOLUTION)

# CODE
================
```

def find_gap(gap):
  if (gap <= 1):
      return 0
  return (gap // 2) + (gap % 2)

def merge(list1, list2, n, m):

  gap = n + m
  gap = find_gap(gap)

  while gap > 0:
    start = 0
    while start + gap < n:
        if (list1[start] > list1[start + gap]):
            list1[start], list1[start + gap] = list1[start + gap], list1[start]
        start += 1

    end = gap - n if gap > n else 0
    while start < n and end < m:
        if (list1[start] > list2[end]):
            list1[start], list2[end] = list2[end], list1[start]
        start += 1
        end += 1
    if (end < m):
      end = 0
      while end + gap < m:
          if (list2[end] > list2[end + gap]):
              list2[end], list2[end + gap] = list2[end + gap], list2[end]
          end += 1
    gap = find_gap(gap)

```