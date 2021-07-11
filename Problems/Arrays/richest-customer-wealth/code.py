def maximumWealth(accounts):
    return max([sum(item) for item in  accounts])
    
if __name__ == "__main__":
    print(maximumWealth([[1,2,3],[3,2,1]]))