def longestConsecutive(nums) -> int:
    stack_nums  = set()
    for item in nums:
        stack_nums.add(item)
    
    seen_count = 0
    max_seen_count = 0
    for item in stack_nums:
        if item in stack_nums:
            if item-1 in stack_nums:
                continue
            else:
                counter_item = item
                seen_count = 1
                while(counter_item+1 in stack_nums):
                    seen_count += 1
                    counter_item += 1
                max_seen_count = max(seen_count, max_seen_count)
                    
    return max_seen_count
    
if __name__ == "__main__":
    print(longestConsecutive([100,4,200,1,3,2]))