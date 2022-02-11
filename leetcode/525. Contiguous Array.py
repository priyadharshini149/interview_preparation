class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
       
        c=0
        m=0
        d=dict({0:-1})
        for i in range(len(nums)):
            if(nums[i]==0):
                c-=1
            elif(nums[i]==1):
                c+=1
            if(c in d):
                m=max(m,i-d[c])
            else:
                d[c]=i
        return m
                
                
                
                
            
        