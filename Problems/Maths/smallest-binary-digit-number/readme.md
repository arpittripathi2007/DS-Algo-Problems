

# Problem Statement
===================

You are given an integer N. You have to find smallest multiple of N which consists of digits 0 and 1 only. Since this multiple could be large, return it in form of a string.

Note:

Returned string should not contain leading zeroes.
For example,

For N = 55, 110 is smallest multiple consisting of digits 0 and 1.
For N = 2, 10 is the answer

# URL
================

https://www.interviewbit.com/problems/smallest-multiple-with-0-and-1/
https://www.geeksforgeeks.org/find-the-smallest-binary-digit-multiple-of-given-number/
(SOLUTIONS)

# CODE
================

```
def multiple(self, A):
    set_visit = [1]
    visited_rem = set([])

    while(len(set_visit)>0):
        check_elem = set_visit.pop(0) #popping latest element to check
        rem = check_elem % A
        if(rem == 0):
            return check_elem
        else:
            if (rem not in visited_rem):
                visited_rem.add(rem)
                set_visit.append(int(str(check_elem)+'0'))
                set_visit.append(int(str(check_elem)+'1'))
```