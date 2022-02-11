
class Solution:
    def maxProfit(self, prices):
        profit = 0
        minimum = prices[0]
        for i in range(len(prices)):
            if(prices[i]>=minimum):
                profit=max(prices[i]-minimum,profit)
            else:
                minimum=prices[i]
        return profit
        
        
            
    