def sumOddLengthSubarrays(arr: List[int])
    sum_ = 0
    length_ = len(arr)
    for i in range(length_):
        sum_ += (((i+1)*(length_-i)+1)//2)*arr[i]
        
    return sum_
    
if __name__ == "__main__":
    print(sumOddLengthSubarrays([1,4,2,5,3]))