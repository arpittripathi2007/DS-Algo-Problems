def thirdMax(nums):
    s=sorted(list(set(nums)))
    return (s[-1] if len(s)<3 else s[-3])
    
if __name__ == "__main__":
    print(thirdMax([2,2,3,1]))