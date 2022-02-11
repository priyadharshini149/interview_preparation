class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        le=1
        for i in range(1,len(nums)):
            if(nums[i]!=nums[i-1]):
                nums[le]=nums[i]
                le+=1
        print(nums)
        return(len(set(nums)))
            
       
        
        