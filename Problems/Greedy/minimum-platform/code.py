def minimumPlatform(n,arr,dep):
  # code here
  plot_needed = result = 1
  arr.sort()
  dep.sort()
  i = 1
  j = 0
  while(i < n and j < n):
      if(arr[i]<=dep[j]):
          plot_needed += 1
          i += 1
      elif(arr[i]>dep[j]):
          plot_needed -= 1
          j += 1
      if(plot_needed > result):
          result = plot_needed
  return result

if __name__ == "__main__":
    print('1st soln:', minimumPlatform(6, [900, 940, 950, 1100, 1500, 1800],[910, 1200, 1120, 1130, 1900, 2000]))
    print('2nd soln:', minimumPlatform(3, [900, 1100, 1235],[1000, 1200, 1240]))


