class Solution(object):
    def sortEvenOdd(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if(len(nums)<=2):
            return nums
        even=[]
        odd=[]
        res=[]
        for i in range(len(nums)):
            if(i%2==0):
                even.append(nums[i])
            else:
                odd.append(nums[i])
        even.sort()
        odd.sort(reverse=True)
        print(even,odd)
        i=0
        j=0
        while(i<len(even)or j<len(odd)):
            if(i<len(even) and j<len(odd)):
                res.append(even[i])
                i+=1
                res.append(odd[j])
                j+=1
            if(i<len(even)):
                    res.append(even[i])
                    i+=1
            if(j<len(odd)):
                    res.append(odd[j])
                    j+=1
            
            
        return res
            
        
        
        