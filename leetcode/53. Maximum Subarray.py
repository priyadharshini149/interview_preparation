class Solution(object):
    def maxSubArray(self, nums):
        maxSum = nums[0]
        currSum = 0
        
        for ele in nums:
            if currSum < 0:
                currSum = 0
            currSum += ele
            print(currSum)
            maxSum = max(currSum, maxSum)
        
        return maxSum