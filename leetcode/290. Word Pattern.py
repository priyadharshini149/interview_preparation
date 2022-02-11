class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        res={}
        l1=list(pattern)
        l2=list(s.split(" "))
        
        if(len(l1)!=len(l2)):
            return False
        if(len(set(l1))!=len(set(l2))):
            return False
        for p,s in zip(l1,l2):
            if(p not in res):
                res[p]=s
            else:
                if(res[p]!=s):
                    return False
        
        return True