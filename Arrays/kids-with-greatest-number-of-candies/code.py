def kidsWithCandies(candies, extraCandies):
    max_elem = max(candies)
    res = [(item+extraCandies) >= max_elem for item in candies]
    return res
    
if __name__ == "__main__":
    print(kidsWithCandies([2,3,5,1,3], 3))