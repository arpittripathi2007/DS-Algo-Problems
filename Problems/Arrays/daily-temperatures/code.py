from typing import List

def dailyTemperatures(temperatures: List[int]) -> List[int]:
    stack = []
    
    res = [0 for i in range(len(temperatures))]
    
    for i in range(len(temperatures)):
        curr_ = temperatures[i]
        
        while stack and temperatures[stack[-1]] < curr_:
            less_index = stack.pop()
            res[less_index] = i - less_index
        stack.append(i)
    return res

if __name__ == "__main__":
    numbers = [73,74,75,71,69,72,76,73]
    print(dailyTemperatures(numbers))