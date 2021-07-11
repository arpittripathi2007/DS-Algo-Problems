# Find The Duplicate Number

# Problem Statement
===================

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.

# URL
================

https://leetcode.com/problems/valid-parentheses/

# CODE
================
```
def isValid(s: str) -> bool:
    array_open = []
    open_bracket = ['(', '{', '[']
    closed_bracket = [')', '}', ']']
    list_s_copy = list(s)
    for item in list(s):
        if item in closed_bracket and len(array_open)==0:
            return False
        elif item in closed_bracket:
            char = item
            current_char = array_open.pop()

            if current_char == '(':
                if char != ")":
                    return False
            if current_char == '{':
                if char != "}":
                    return False
            if current_char == '[':
                if char != "]":
                    return False
        else:
            array_open.append(item)
    if len(array_open)>0:
        return False
    else:
        return True
    
```



