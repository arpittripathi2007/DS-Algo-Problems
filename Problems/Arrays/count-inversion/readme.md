

# Problem Statement (HARD)
===================

TInversion Count for an array indicates – how far (or close) the array is from being sorted. If the array is already sorted, then the inversion count is 0, but if the array is sorted in the reverse order, the inversion count is the maximum. 
Formally speaking, two elements a[i] and a[j] form an inversion if a[i] > a[j] and i < j 
Example: 

Input: arr[] = {8, 4, 2, 1}
Output: 6

Explanation: Given array has six inversions:
(8, 4), (4, 2), (8, 2), (8, 1), (4, 1), (2, 1).


Input: arr[] = {3, 1, 2}
Output: 2


# URL
================

https://www.geeksforgeeks.org/counting-inversions/

# CODE
================

```
def merge(list_given, temp_arr, left, mid, right):
    i = left
    j = mid + 1
    k = left
    count_inversion = 0

    while(i <= mid-1 and j <= right):
        if list_given[i] <= list_given[j]:
            temp_arr[k] = list_given[i]
            i += 1
            k += 1
        else:
            list_given[k] = list_given[j]
            count_inversion += (mid-i)
            j += 1
            k += 1

    while i <= mid-1:
        temp_arr[k] = list_given[i]
        i += 1
        k += 1
    while j <= right:
        temp_arr[k] = list_given[j]
        j += 1
        k += 1
    for loop_var in range(left, right + 1):
        list_given[loop_var] = temp_arr[loop_var]
    return count_inversion


def mergeSort(list_given, temp_arr, left, right):
    count_inversion = 0
    if left < right:
        mid = (left+ right)//2

        count_inversion += mergeSort(list_given, temp_arr, left, mid)
        count_inversion += mergeSort(list_given, temp_arr, mid+1, right)

        count_inversion += merge(list_given, temp_arr, left, mid, right)
    return count_inversion

```