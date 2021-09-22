## Factors of number

You are given 2 numbers (n , m); the task is to find n√m (nth root of m).

Example 1:

Input: n = 2, m = 9
Output: 3
Explanation: 32 = 9


# CODE
================
```
def NthRoot(n, m):
    # Code here
    start = 0
    end = 9
    eps = 1e-9

    mid = (start + end)/2


    while(mid ** n != float(m)):
        if(mid**n > m):
            end = mid-1
        else:
            start = mid+1
        mid = (start+end)/2

    return round(mid)
    
```
