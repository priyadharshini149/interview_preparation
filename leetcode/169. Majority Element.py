class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a=dict(Counter(nums))
        a=sorted(a.items(),key=lambda x:x[1])
        return(a[len(a)-1][0])
        