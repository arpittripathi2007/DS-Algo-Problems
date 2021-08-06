def maxLen(n, arr):
    seen_values = {}
    max_length = 0
    sum_values = 0
    for i in range(n):
        sum_values += arr[i]
        if sum_values == 0:
            max_length = max(max_length, i+1)
        elif sum_values in seen_values:
            max_length = max(max_length, i - seen_values[sum_values])
        else:
            seen_values[sum_values] = i
    return max_length
    
if __name__ == "__main__":
    print(maxLen(8, [15,-2,2,-8,1,7,10,23]))