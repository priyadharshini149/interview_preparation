class Solution(object):
    def validMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        n=len(arr)
        if(len(arr)<3):
            return False
        i=0
        j=n-1
        
        while(i<n-1 and arr[i]<arr[i+1]):
            i+=1
        while(j>0 and arr[j]<arr[j-1]):
            j-=1
        
        return(i==j and i!=n-1 and j!=0)