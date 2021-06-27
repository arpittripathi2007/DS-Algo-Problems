def shuffle(nums, n):
    res = []
    for i in range(n):
        res.append(nums[i])
        res.append(nums[i+n])
    return res
    
if __name__ == "__main__":
    print(shuffle([2,5,1,3,4,7], 3))