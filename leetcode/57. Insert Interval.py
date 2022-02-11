class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        intervals.append(newInterval)
        intervals=sorted(intervals,key=lambda x:x[0])
        ans=[]
        ans.append(intervals[0])
        for start,end in intervals[1:]:
            last=ans[-1][1]
            if(last>=start):
                ans[-1][1]=max(end,last)
            else:
                ans.append([start,end])
        return(ans)
        
        