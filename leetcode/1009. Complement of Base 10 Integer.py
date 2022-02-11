class Solution(object):
   
        
            
    def bitwiseComplement(self, n):
        """
        :type n: int
        :rtype: int
        """
        com=""
        b=bin(n).replace("0b","")   
        print(b)
        for i in b:
            if i=='0':
                com+='1'
            else:
                com+='0'
        return(int(com,2))