def hammingWeight(n):
    return sum([(n>>i)&1 for i in range(32)])
    
if __name__ == "__main__":
    print(hammingWeight('00000000000000000000000000001011'))