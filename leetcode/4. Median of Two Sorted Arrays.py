class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        res=sorted(nums1+nums2)
        if(len(res)%2!=0):
            return res[len(res)//2]
        else:
            return (res[len(res)//2]+res[len(res)//2-1])/float(2)