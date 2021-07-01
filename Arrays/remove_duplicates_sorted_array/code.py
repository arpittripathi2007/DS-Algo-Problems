def removeDuplicates(nums):
    count_a = len(nums)
    point_1 = 0
    point_2 = 0
    while(point_2< count_a):
        if(nums[point_1] == nums[point_2]):
            point_2 += 1
        else:
            point_1 += 1
            nums[point_1] = nums[point_2]
            point_2 += 1
    return point_1+1
    
if __name__ == "__main__":
    print(removeDuplicates([0,0,1,1,1,2,2,3,3,4]))