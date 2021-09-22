def sepZeroOne(arr_):
    """
    Do not return anything, modify matrix in-place instead.
    """
    start = 0
    end = len(arr_)-1

    while(start<end):
        while(arr_[start] == 0):
            start += 1
        while(arr_[end] == 1):
            end -= 1

        arr_[start], arr_[end] = arr_[end], arr_[start]
        start += 1
        end -= 1
    return arr_

    
if __name__ == "__main__":
    print(sepZeroOne([0, 1, 0, 1, 0, 0, 1, 1, 1, 0]))