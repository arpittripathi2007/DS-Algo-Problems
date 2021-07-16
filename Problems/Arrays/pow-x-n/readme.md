

# Problem Statement
===================

Implement pow(x, n), which calculates x raised to the power n (i.e., xn).

 

Example 1:

Input: x = 2.00000, n = 10
Output: 1024.00000
Example 2:

Input: x = 2.10000, n = 3
Output: 9.26100


# URL
================

https://leetcode.com/problems/powx-n/


# CODE
================
```
def myPow(x: float, n: int) -> float:
    num = n if n >= 0 else n*-1
    ans = 1
    while(num > 0):
        if(num % 2 == 1):
            ans = ans * x
            num = num - 1
        else:
            x = x * x
            num = num / 2
            
    ans  = ans if n >= 0 else 1/(ans)
    
    return ans

```