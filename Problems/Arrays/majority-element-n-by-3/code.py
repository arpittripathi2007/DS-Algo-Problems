from math import inf

def majorityElement(nums):
    count1 = 0
    count2 = 0
    
    num1 = -inf
    num2 = -inf
    res = []
    
    for item in nums:
        if(item == num1):
            count1 += 1
        elif(item == num2):
            count2 += 1
        elif(count1 == 0):
            num1 = item
            count1 = 1
        elif(count2 == 0):
            num2 = item
            count2 = 1
        else:
            count1 -= 1
            count2 -= 1
    
    count1 = 0
    count2 = 0
    
    for item in nums:
        if(num1 == item):
            count1 += 1
        if(num2 == item):
            count2 += 1
            
    if(count1 > len(nums)/3):
        res.append(num1)
    if(count2 > len(nums)/3):
        res.append(num2)
    return res
    
if __name__ == "__main__":
    print(majorityElement([1,2]))