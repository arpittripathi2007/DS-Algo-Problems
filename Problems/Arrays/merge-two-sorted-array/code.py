def find_gap(gap):
  if (gap <= 1):
      return 0
  return (gap // 2) + (gap % 2)

def merge(list1, list2, n, m):

  gap = n + m
  gap = find_gap(gap)

  while gap > 0:
    start = 0
    while start + gap < n:
        if (list1[start] > list1[start + gap]):
            list1[start], list1[start + gap] = list1[start + gap], list1[start]
        start += 1

    end = gap - n if gap > n else 0
    while start < n and end < m:
        if (list1[start] > list2[end]):
            list1[start], list2[end] = list2[end], list1[start]
        start += 1
        end += 1
    if (end < m):
      end = 0
      while end + gap < m:
          if (list2[end] > list2[end + gap]):
              list2[end], list2[end + gap] = list2[end + gap], list2[end]
          end += 1
    gap = find_gap(gap)

    
if __name__ == "__main__":
    list1 = [10, 27, 38, 43, 82]
    list2 = [3, 9]
    merge(list1, list2, len(list1), len(list2))
    print(list1+list2)
