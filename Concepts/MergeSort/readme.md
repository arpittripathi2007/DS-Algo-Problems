

# MERGE SORT
===================

## Divide and Conquer Algorithm
Alright, time for a definition. The merge sort algorithm is a sorting algorithm that sorts a collection by breaking it into half. It then sorts those two halves, and then merges them together, in order to form one, completely sorted collection.

The basic steps of a d&c algorithm can be boiled down to these three steps:
* Divide and break up the problem into the smallest possible “subproblem”, of the exact same type.
* Conquer and tackle the smallest subproblems first. Once you’ve figured out a solution that works, use that exact same technique to solve the larger subproblems — in other words, solve the subproblems recursively.
* Combine the answers and build up the smaller subproblems until you finally end up applying the same solution to the larger, more complicated problem that you started off with!

## Important Characteristics of Merge Sort:
* Merge Sort is useful for sorting linked lists.
* Merge Sort is a stable sort which means that the same element in an array maintain their original positions with respect to each other.
* Overall time complexity of Merge sort is O(nLogn). It is more efficient as it is in worst case also the runtime is O(nlogn)
* The space complexity of Merge sort is O(n). This means that this algorithm takes a lot of space and may slower down operations for the last data sets.