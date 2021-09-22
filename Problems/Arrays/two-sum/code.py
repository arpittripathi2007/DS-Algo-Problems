from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    visited_key = {}
    
    for index, item in enumerate(nums):
        if target-item in visited_key:
            return [visited_key[target-item], index]
        else:
            visited_key[item] = index
    
def twoSumNoIndex(nums: List[int], target: int) -> List[int]:
    visited_key = set()
    
    for item in nums:
        ## search in set in O(1)
        if target-item in visited_key:
            return item, target-item
        else:
            visited_key.add(item)

if __name__ == "__main__":
    numbers = [2,7,11,15]
    target = 9
    print(twoSum(numbers, target))
    print(twoSumNoIndex(numbers, target))