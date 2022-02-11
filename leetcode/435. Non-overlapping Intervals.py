class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        intervals=sorted(intervals,key=lambda x:x[1])
        print(intervals)
        ans=[]
        end=intervals[0][1]
        length=1
        for i in range(1,len(intervals)):
            if(intervals[i][0]>=end):
                length+=1
                end=intervals[i][1]
        print(length)       
        return(len(intervals)-length)
    

        