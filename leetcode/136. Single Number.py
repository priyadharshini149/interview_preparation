class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a=dict(Counter(nums))
        for i in a.items():
            if(i[1]==1):
                return i[0]
        
        