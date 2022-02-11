class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        r=dict(Counter(nums))
        l=0
        for i in r.items():
            if(i[1]>2):
                e=i[1]-2
                while(e>0):
                    nums.pop(nums.index(i[0]))
                    nums.append(i[0])
                    l+=1
                    e-=1
        return(len(nums)-l)