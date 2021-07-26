

# QUICK SORT
===================
It is also called partition exchange sort. It is used recursive calls for sorting elements. It picks an element as pivot and partitions the given array around the picked pivot.There are many different versions of quickSort that pick pivot in different ways.
* Always pick first element as pivot.
* Always pick last element as pivot (implemented below)
* Pick a random element as pivot.
* Pick median as pivot.

The key process in quickSort is partition().

### Divide: 
The list A[low … high] is partitioned into two non-empty sub list A[low…pi] and A[pi+1…high].
### Conquer: 
The two sub list A[low…pi] and A[pi+1…high] are sorted by recursive calls to Quick sort.
### Algorithm:
* If there are one or no elements in the list to be sorted , return
* Pick an element in the list to serve as the “pivot” point . Usually the left-most element in the list is used . However , we can also used other elements like last or medium as “pivot” .
* Split list into two parts — one with elements larger than the pivot and the other with elements smaller than the pivot.
* Recursively repeat the algorithm for both halves of the original array.

## Time and Space Complexity
Each time I actually break the array into 2 while in each array (or subarray) I need to check every element, so the time complexity will be O(NlogN).
Space complexity is O(logN) since even the input array increase, the space used will increase due to recursive calling.