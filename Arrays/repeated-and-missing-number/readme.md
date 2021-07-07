

# Problem Statement
===================

You are given a read only array of n integers from 1 to n.

Each integer appears exactly once except A which appears twice and B which is missing.

Return A and B.

Note: Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Note that in your output A should precede B.

Example:

Input:[3 1 2 5 3] 

Output:[3, 4] 

A = 3, B = 4

# URL
================

https://www.interviewbit.com/problems/repeat-and-missing-number-array/

https://www.geeksforgeeks.org/find-a-repeating-and-a-missing-number/ 
(SOLUTION)

# CODE
================
```
def repeatedNumber(A):
    xor_A = A[0]
    x, y = 0, 0
    for item in A[1:]:
        xor_A = xor_A ^ item

    for i in range(1, len(A)+1):
        xor_A = xor_A ^ i

    right_most_bit = xor_A & ~(xor_A -1)

    for item in A:
        if(item & right_most_bit) != 0:
            x = x ^ item
        else:
            y = y ^ item
    
    for i in range(1, len(A)+1):
        if(i & right_most_bit) != 0:
            x = x ^ i
        else:
            y = y ^ i 
    return [x , y]


```