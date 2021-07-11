
# Problem Statement
===================

Given an array of integers arr, return true if and only if it is a valid mountain array.

Recall that arr is a mountain array if and only if:

arr.length >= 3
There exists some i with 0 < i < arr.length - 1 such that:
arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
arr[i] > arr[i + 1] > ... > arr[arr.length - 1]

# URL
================

https://leetcode.com/problems/valid-mountain-array/

# CODE
================
```
def validMountainArray(A):
    N = len(A)
    i = 0

    # walk up
    while i+1 < N and A[i] < A[i+1]:
        i += 1

    # peak can't be first or last
    if i == 0 or i == N-1:
        return False

    # walk down
    while i+1 < N and A[i] > A[i+1]:
        i += 1

    return i == N-1
```