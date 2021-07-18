

# Binary Search
===================

## Time Complexity
### Best Case O(1)
### Average Case O(log n)
### Worst Case O(log n)

## Algorithm
* Given a list L of n elements with values or records L0, L1, …, Ln-1, sorted in ascending order, and given key/target value K, binary search is used to find the index of K in L
* Set a variable start to 0 and another variable end to n-1(size of the list)
* if start > end break the algorithm, as it works only on sorted lists
calculate mid as (start + end)/2
* if the key element is equal to mid, the search is done return position of mid
greater than mid, set start to mid + 1 and repeat from step 2
less than mid, set end to mid — 1 and repeat from step 2