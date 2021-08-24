def lastStoneWeight(stones) -> int:
    n = len(stones)
    stones.sort(reverse=True)
    
    if n==1:
        return stones[0]
        
    while(n>1):
        fir = stones.pop(0)
        sec = stones.pop(0)
        
        stones.append(fir-sec)
        return lastStoneWeight(stones)
    
if __name__ == "__main__":
    print(lastStoneWeight([2,7,4,1,8,1]))