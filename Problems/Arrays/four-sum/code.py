from typing import List

def fourSum(nums: List[int], target: int) -> List[List[int]]:
    nums.sort()

    if len(nums) < 4:
        return []

    else:

        temp = set()

        for i in range(len(nums) - 3):
            for j in range(i + 1, len(nums) - 2):

                p = j + 1
                q = len(nums) - 1

                while p < q:

                    if (nums[i] + nums[j]) == target - (nums[p] + nums[q]):

                        temp.add((nums[i], nums[j], nums[p], nums[q]))
                        p += 1
                        q -= 1

                    elif (nums[i] + nums[j]) > target - (nums[p] + nums[q]):
                        q -= 1

                    else:
                        p += 1

        return (temp)
    
if __name__ == "__main__":
    numbers = [1,0,-1,0,-2,2]
    target = 0
    print(fourSum(numbers, target))