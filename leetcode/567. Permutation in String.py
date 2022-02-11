from itertools import permutations
class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        s1=sorted(s1)
        end=len(s1)
        i=0
        while(end<=len(s2)):
            if(s1==sorted(s2[i:end])):
                return True
            end+=1
            i+=1
        return False