from __future__ import print_function


def MergeSort(list_given):
    if len(list_given) > 1:
        mid = len(list_given)//2

        left_partition = list_given[:mid]
        right_partition = list_given[mid:]

        MergeSort(left_partition)
        MergeSort(right_partition)

        i=j=k=0

        while(i < len(left_partition) and j < len(right_partition)):
            if left_partition[i] < right_partition[j]:
                list_given[k] = left_partition[i]
                i += 1
                k += 1
            else:
                list_given[k] = right_partition[j]
                j += 1
                k += 1

        while i < len(left_partition):
            list_given[k] = left_partition[i]
            i += 1
            k += 1
        while j < len(right_partition):
            list_given[k] = right_partition[j]
            j += 1
            k += 1
    return list_given



if __name__ == "__main__":
    res = MergeSort([29,10,5,2,1,100,200])
    print(res)

    