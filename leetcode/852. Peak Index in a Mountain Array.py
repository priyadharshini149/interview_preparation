class Solution(object):
    def peakIndexInMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        s=0
        end=len(arr)
        while(s+1<end):
            mid=(end+s)//2
            if arr[mid-1]<arr[mid] and arr[mid+1]<arr[mid]:
                return mid
            elif arr[mid-1]<arr[mid]:
                s=mid
            else:
                end=mid
        return s
    
    