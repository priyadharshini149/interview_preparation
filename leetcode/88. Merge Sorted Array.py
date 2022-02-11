class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        
        k=0
        le=m+n
        
        for i in range(m,le):
            if(nums1[i]==0):
                nums1[i]=nums2[k]
                k+=1
        nums1.sort()
        
       
        