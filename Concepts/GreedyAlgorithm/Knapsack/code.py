from __future__ import print_function

def swap(list_given, left, right):
    temp = list_given[left]
    list_given[left] = list_given[right]
    list_given[right] = temp

def pivot_index(list_given, first, last):
    ## Selecting first element as pivot element
    pivot_item = list_given[first]
    
    left = first
    right = last
    while(left < right):
        while(list_given[left] <= pivot_item):
            left += 1
           
        while(list_given[right] > pivot_item):
            right -= 1
            
        if left < right :
            swap(list_given,left,right)
            
    list_given[first] = list_given[right]
    list_given[right] = pivot_item
    
    return right


def quickSort(list_given, first, last):
    ## Sort in ascending order
    
    if last > first :
        pivot = pivot_index(list_given, first, last)
        quickSort(list_given, first, pivot-1)
        quickSort(list_given, pivot+1, last)


if __name__ == "__main__":
    list_given = [6,8,1,4,5,3,7,2]
    last = len(list_given)-1
    quickSort(list_given, 0, last)
    print(list_given)

    