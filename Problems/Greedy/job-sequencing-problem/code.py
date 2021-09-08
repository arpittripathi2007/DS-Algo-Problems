class JobDS:
  def __init__(self, id, deadline, profit):
    self.id = id
    self.deadline = deadline
    self.profit = profit

def JobScheduling(Jobs,n):
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

if __name__ == "__main__":
    jobs_input = [(1,4,20),(2,1,10),(3,1,40),(4,1,30)]
    jobs_ds = []
    for item in jobs_input:
      jobs_ds.append(JobDS(item[0], item[1], item[2]))
      
    print('1st soln:', JobScheduling(jobs_ds, 6))

