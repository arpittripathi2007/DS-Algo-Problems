

# Problem Statement
===================

Given a string s, find the length of the longest substring without repeating characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

# URL
================

https://leetcode.com/problems/longest-substring-without-repeating-characters/

# CODE
================

```
def lengthOfLongestSubstring(s):
    l = 0
    r = 0
    seen_dict = {}
    length_max = 0
    len_s = len(s)
    
    while(r < len_s):
        if s[r] in seen_dict:
            l = max(l, seen_dict[s[r]]+1)
        seen_dict[s[r]] = r
        length_max = max(length_max, r-l+1)
        r += 1
    return length_max
```