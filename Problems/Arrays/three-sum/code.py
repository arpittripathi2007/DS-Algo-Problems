def threeSum(nums):
    res = []
    nums.sort()
    for i, num in enumerate(nums):
        if i>0 and num == nums[i-1]:
            continue
        left = i +1 
        end = len(nums)-1
        
        while left < end:
            three_sums = num + nums[left] + nums[end]
            
            if three_sums < 0:
                left += 1
            elif three_sums > 0:
                end -= 1
            else:
                res.append([num, nums[left], nums[end]])
                left += 1
                while(nums[left] == nums[left-1] and left < end):
                    left += 1
    return res
    
if __name__ == "__main__":
    numbers = [-1,0,1,2,-1,-4]
    target = 9
    print(threeSum(numbers))