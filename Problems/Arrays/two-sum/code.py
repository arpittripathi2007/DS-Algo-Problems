from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    visited_key = {}
    
    for index, item in enumerate(nums):
        if target-item in visited_key:
            return [visited_key[target-item], index]
        else:
            visited_key[item] = index
    
if __name__ == "__main__":
    numbers = [2,7,11,15]
    target = 9
    print(twoSum(numbers, target))