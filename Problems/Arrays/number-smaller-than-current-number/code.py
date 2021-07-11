def smallerNumbersThanCurrent(self, nums):
    res = []
    for i in nums:
        count = 0
        for j in nums:
            if(j < i):
                count += 1
        res.append(count)
    return res
    
if __name__ == "__main__":
    print(smallerNumbersThanCurrent([8,1,2,2,3]))