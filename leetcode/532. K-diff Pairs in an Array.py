class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        s=set(nums)
        c=0
        if k==0:
            for i in s:
                if(nums.count(i)>1):
                    c+=1
        else:
            for i in s:
                if(i+k in nums):
                    c+=1
        return c 
    
    
                    