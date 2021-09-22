from typing import List

def rotate(nums: List[int], k: int) -> None:
    k=k%len(nums)
    ##     [5,6,7] + [1,2,3,4]
    nums[:]=nums[-k:]+nums[:-k]
    return nums

def rotate2(nums: List[int], k: int) -> None:
    nums = nums[::-1]
    nums =  nums[:k][::-1] +  nums[k:][::-1]
    return nums
    
if __name__ == "__main__":
    print(rotate([1,2,3,4,5,6,7], 3))
    print(rotate2([1,2,3,4,5,6,7], 3))