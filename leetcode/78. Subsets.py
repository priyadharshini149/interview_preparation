class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        s=[[]]
        for i in nums:
            t=[]
            for j in s:
                t.append(j+[i])
            s+=t
        return(s)   