from __future__ import print_function


def BinarySearchIterative(list_given, search_value):
    low = 0
    high = len(list_given) - 1

    found = False

    while(low <= high):
        mid = (low + high)//2
        if search_value == list_given[mid]:
            return True

        elif search_value < list_given[mid]:
            high = mid - 1
        else:
            low = mid + 1 
    return found

def BinarySearchRecurssive(list_given, search_value, low, high):
    while(low <= high):
        mid = (low + high)//2
        if search_value == list_given[mid]:
            return True
        elif search_value < list_given[mid]:
            return BinarySearchRecurssive(list_given, search_value, low,  mid - 1)
        else:
            return BinarySearchRecurssive(list_given, search_value, mid+1,  high)

    return False
    
def print_res(found):
    if found:
        print('Key is Found')
    else:
        print('Key is not Found')



if __name__ == "__main__":
    res = BinarySearchIterative([29,10,5,2,1, 100, 200], 100)
    print_res(res)
    res = BinarySearchIterative([29,10,5,2,1, 250, 200], 100)
    print_res(res)

    low = 0
    list_given = [29,10,5,2,1, 100, 200]
    high = len(list_given) - 1
    res = BinarySearchRecurssive(list_given, 100, low, high)
    print_res(res)


    