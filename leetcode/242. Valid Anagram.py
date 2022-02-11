class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        l1=list(s)
        l2=list(t)
        l1.sort()
        l2.sort()
        return(l1==l2)


class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        a=Counter(s)
        b=Counter(t)
       
        if(len(s)>len(t)):
            for i in range(len(s)):
                if(a[s[i]]==b[s[i]]):
                    continue
                else:
                    return False
            
        else:
            for i in range(len(t)):
                if(a[t[i]]==b[t[i]]):
                    continue
                else:
                    return False
        return True
            