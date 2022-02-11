class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        res=""
        
            
        for i in range(len(min(strs))):
            if(strs[0]==""):
                return ""
            com=strs[0][i]
            for s in strs:
                if(s[i]!=com):
                    return res
            res+=com
        return(res)
        
            
            
      