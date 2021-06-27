def numIdenticalPairs(nums):
    count = 0
    length = len(nums)
    for i in range(length-1):
        count += nums[i+1: length].count(nums[i])
    return count
    
if __name__ == "__main__":
    print(numIdenticalPairs([1,1,1,1]))