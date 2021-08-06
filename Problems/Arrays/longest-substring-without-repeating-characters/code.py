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
    
if __name__ == "__main__":
    print(lengthOfLongestSubstring('abcabcbb'))