def majorityElement(nums) -> int: ## MOORE VOTING ALGORITHM
    count = 0
    candidate = 0
    for item in nums:
        if(count == 0):
            candidate = item
        if(candidate == item):
            count += 1
        else:
            count -= 1
    return candidate
    
if __name__ == "__main__":
    print(majorityElement([2,2,1,1,1,2,2]))