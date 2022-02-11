class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        st=0
        e=len(numbers)-1
        while(st<=e):
            s=numbers[st]+numbers[e]
            if(s==target):
                return [st+1,e+1]
            elif(s<target):
                st+=1
            else:
                e-=1 