

# Problem Statement
===================

Given a set of N jobs where each jobi has a deadline and profit associated with it. Each job takes 1 unit of time to complete and only one job can be scheduled at a time. We earn the profit if and only if the job is completed by its deadline. The task is to find the number of jobs done and the maximum profit.

Note: Jobs will be given in the form (Jobid, Deadline, Profit) associated with that Job.


Example 1:

Input:
N = 4
Jobs = {(1,4,20),(2,1,10),(3,1,40),(4,1,30)}
Output:
2 60
Explanation:
Job1 and Job3 can be done with
maximum profit of 60 (20+40).



# URL
================

https://practice.geeksforgeeks.org/problems/job-sequencing-problem-1587115620/1#

# CODE
================

```
class JobDS:
  def __init__(self, id, deadline, profit):
    self.id = id
    self.deadline = deadline
    self.profit = profit
      
def JobScheduling(self,Jobs,n):
  # code here
  count_job = 0
  job_profit = 0
  Jobs.sort(key= lambda x: x.profit, reverse=True)
  max_deadline = 0
  for item in Jobs:
    if item.deadline >= max_deadline:
      max_deadline = item.deadline
  res = [-1]*max_deadline
  for item in Jobs:
    index = item.deadline -1
    while(index >=0):
      if(res[index] == -1):
        res[index] = item.profit
        count_job += 1
        job_profit += item.profit
        break
      index -= 1
              
  return [count_job, job_profit]
```