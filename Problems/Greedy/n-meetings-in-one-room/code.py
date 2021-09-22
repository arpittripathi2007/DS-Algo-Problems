class MeetingDs:
    def __init__(self, start, end, pos):
      self.start = start
      self.end = end
      self.pos = pos

class Solution:
    #Function to find the maximum number of meetings that can
    #be performed in a meeting room.
    def maximumMeetings(self,n,start,end):
      # code here
      start = list(start)
      end = list(end)
      collectionMeeting = []
      for i in range(n):
        collectionMeeting.append(MeetingDs(start[i], end[i], i))
      
      collectionMeeting.sort(key = lambda x: x.end)

      current_interval = -1
      res = []
      for item in collectionMeeting:
        if item.start > current_interval and item.end > current_interval:
          current_interval = item.end
          res.append(item)
      return(len(res))

if __name__ == "__main__":
    class_obj = Solution()
    print('1st soln:', class_obj.maximumMeetings(6, [1,3,0,5,8,5],[2,4,6,7,9,9]))
    print('2nd soln:', class_obj.maximumMeetings(3, [10, 12, 20],[20, 25, 30]))


