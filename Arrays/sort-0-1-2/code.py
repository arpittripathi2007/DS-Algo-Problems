def sortColors(nums):
    low = 0
    mid = 0
    high = len(nums)-1
    while(mid<=high):
        if nums[mid] == 0:
            temp = nums[low]
            nums[low] = nums[mid]
            nums[mid] = temp
            low += 1
            mid += 1
        elif nums[mid] == 1:
            mid += 1
            
        else:
            nums[mid]==2
            temp = nums[mid]
            nums[mid] = nums[high]
            nums[high] = temp
            high -= 1
    return nums

if __name__ == "__main__":
    print(sortColors([2,0,2,1,1,0]))