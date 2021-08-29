from typing import List
from math import inf

def findMaxConsecutiveOnes(nums: List[int]) -> int:
    count = 0
    max_count = 0
    
    for item in nums:
        if item == 1:
            count += 1
        else:
            max_count = max(max_count, count)
            count = 0
    max_count = max(max_count, count)
    return max_count
    
if __name__ == "__main__":
    print(findMaxConsecutiveOnes([1,1,0,1,1,1]))