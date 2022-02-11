class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        
        def add(num):
            if(len(str(num))==1):
                return num
            l=list(str(num))
            s=0
            for i in l:
                s+=int(i)
            return add(s)
        return(add(num))
        
        