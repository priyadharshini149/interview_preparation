class Solution(object):
    def removeCoveredIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        intervals=sorted(intervals,key=lambda x:(x[0],-x[1]))
        print(intervals)
        length=len(intervals)
        end=intervals[0][1]
        for i in range(1,len(intervals)):
            if(intervals[i][1]<=end):
                length-=1
            else:
                end=intervals[i][1]
        print(intervals)
        return(length)
            
            
        