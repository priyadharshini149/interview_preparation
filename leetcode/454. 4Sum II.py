class Solution(object):
    def fourSumCount(self, nums1, nums2, nums3, nums4):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type nums3: List[int]
        :type nums4: List[int]
        :rtype: int
        """
        c=0
        d=defaultdict(int)
        for i in nums1:
            for j in nums2:
                d[i+j]+=1
        
        for i in nums3:
            for j in nums4:
                c+=d[-(i+j)]
        return c
                            