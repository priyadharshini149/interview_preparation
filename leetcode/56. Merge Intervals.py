class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals=sorted(intervals,key=lambda x:x[0])
        print(intervals)
        ans=[]
        ans.append(intervals[0])
        for start,end in intervals[1:]:
            last=ans[-1][1]
            if(last>=start):
                ans[-1][1]=max(last,end)
            else:
                ans.append([start,end])
        return ans
                
            
            