class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        a=Counter(magazine)
        b=Counter(ransomNote)
        
        for i in b:
            if(a[i]<b[i]):
                 return False
        return True
           
        
        