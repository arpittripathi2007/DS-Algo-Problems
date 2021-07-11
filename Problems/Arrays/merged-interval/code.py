def merge(intervals):
    intervals.sort()
    temp_interval = intervals[0]
    res_interval = []

    for item in intervals:
        if item[0] <= temp_interval[1]:
            temp_interval[1] = max(temp_interval[1], item[1])
        else:
            res_interval.append(temp_interval)
            temp_interval = item
    res_interval.append(temp_interval)   
    return res_interval
    
if __name__ == "__main__":
    list1 = [[1,3],[2,6],[8,10],[15,18],[17, 29], [45, 54]]
    print(merge(list1))
