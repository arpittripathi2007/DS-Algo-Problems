class Solution:
  def find_subset(self, index, nums, ds, ans_):
    ans_.append(list(ds))
    for i in range(index, len(nums)):
      if(i != index and nums[i]==nums[i-1]):
        continue
      ds.append(nums[i])
      self.find_subset(i+1, nums, ds, ans_)
      ds.pop()
        
  def subsetsWithDup(self, nums):
    ds = []
    ans_ = []
    nums.sort()
    self.find_subset(0, nums,ds, ans_)
    x = 20 000
    print(x)
    return ans_
    
class_obj = Solution()
print(class_obj.subsetsWithDup([1,2,2]))