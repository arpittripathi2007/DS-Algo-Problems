def twoSum(numbers, target):
    first = 0
    end = len(numbers)-1
    
    while(first < end):
        if(numbers[first]+numbers[end])< target:
            first += 1
        elif(numbers[first]+numbers[end] > target):
            end -= 1
        else:
            return [first+1, end+1]
    
if __name__ == "__main__":
    numbers = [2,7,11,15]
    target = 9
    print(twoSum(numbers, target))