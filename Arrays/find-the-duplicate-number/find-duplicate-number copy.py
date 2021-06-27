def findDuplicate(nums):
    slow = nums[0]
    fast = nums[0]

    slow = nums[slow]
    fast = nums[nums[fast]]
    while(slow != fast):
        slow = nums[slow]
        fast = nums[nums[fast]]
   
    fast = nums[0]
    while(slow != fast):
        slow = nums[slow]
        fast = nums[fast]
    
    return slow
    
if __name__ == "__main__":
    print(findDuplicate([1,3,4,2,2]))