class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        m=float("-inf")
        s=0
        for i in range(len(accounts)):
            s=sum(accounts[i])
            m=max(m,s)
            s=0
        return(m)
        