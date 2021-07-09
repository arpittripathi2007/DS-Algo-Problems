def find_gap(gap):
  if (gap <= 1):
      return 0
  return (gap // 2) + (gap % 2)

def maxSubArray(nums):
       
    maxSum = nums[0]
    sum_ = 0
    
    for item in nums:
        sum_ += item
        if maxSum < sum_:
            maxSum = sum_
        sum_ = 0 if sum_ < 0 else sum_
        
    return maxSum
    
if __name__ == "__main__":
    list1 = [-2,1,-3,4,-1,2,1,-5,4]
    maxSum = maxSubArray(list1)
    print(maxSum)
