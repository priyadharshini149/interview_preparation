class Solution(object):
    def minimumCost(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        cost.sort()
        sum=0
        i=len(cost)-1
        while(i>=0):
            if(i>=0):
                sum+=cost[i]
            i-=1
            if(i>=0):
                sum+=cost[i]
            i-=2
            
        return(sum)
                
            
            