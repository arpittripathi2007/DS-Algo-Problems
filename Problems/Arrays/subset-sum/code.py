class Solution:
  def recursive_sum(self, index, sum_, arr, N, sum_subset):
    if(index == N):
      sum_subset.append(sum_)
      return
    # picking up element in subset tree
    self.recursive_sum(index+1, arr[index]+sum_, arr, N, sum_subset)
    # not picking up
    self.recursive_sum(index+1, sum_, arr, N, sum_subset)
    return sum_subset
        
  def subsetSums(self, arr, N):
    res = self.recursive_sum(0, 0, arr, N, [])
    if res is not None:
      res.sort()
      return res
    
class_obj = Solution()
print(class_obj.subsetSums([2, 3], 2))