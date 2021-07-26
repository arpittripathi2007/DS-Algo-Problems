from __future__ import print_function

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


if __name__ == "__main__":
    arr = [1, 20, 6, 4, 5]
    n = len(arr)
    temp_arr = [0]*n
    result = mergeSort(arr, temp_arr,0, n-1)
    print("Number of inversions are", result)
    print(result)

    