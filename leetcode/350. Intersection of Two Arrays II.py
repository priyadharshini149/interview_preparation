class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        res=[]
        if(len(nums2)<len(nums1)):
            for i in nums2:
                if(i in nums1):
                    res.append(i)
                    nums1.remove(i)
            return(res)
        else:
            for i in nums1:
                if(i in nums2):
                    res.append(i)
                    nums2.remove(i)
            return(res) 
      
        