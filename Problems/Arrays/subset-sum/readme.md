

# Problem Statement
===================

Given a list arr of N integers, print sums of all subsets in it.

Example 1:

Input:
N = 2
arr[] = {2, 3}
Output:
0 2 3 5
Explanation:
When no elements is taken then Sum = 0.
When only 2 is taken then Sum = 2.
When only 3 is taken then Sum = 3.
When element 2 and 3 are taken then 
Sum = 2+3 = 5.

# URL
================

https://practice.geeksforgeeks.org/problems/subset-sums2234/1#


# CODE
================
```
def recursive_sum(index, sum_, arr, N, sum_subset):
    if(index == N):
        sum_subset.append(sum_)
        return
    # picking up element in subset tree
    self.recursive_sum(index+1, arr[index]+sum_, arr, N, sum_subset)
    # not picking up
    self.recursive_sum(index+1, sum_, arr, N, sum_subset)
    return sum_subset
        
	def subsetSums(arr, N):
        # code here
        res = self.recursive_sum(0, 0, arr, N, [])
        if res is not None:
            res.sort()
            return res

```