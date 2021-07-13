from typing import List
from math import inf

def maxProfit(prices: List[int]) -> int:
    min_stock = float(inf)
    max_profit = 0
    
    for item in prices:
        min_stock = min(min_stock, item)
        max_profit = max(max_profit, item-min_stock)
        
    return max_profit
    
if __name__ == "__main__":
    print(maxProfit([7,1,5,3,6,4]))