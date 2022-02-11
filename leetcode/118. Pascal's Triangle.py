class Solution(object):
    def generate(self, num):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        res=[]
        l1=[]
        for i in range(1,num+1):
            if(i==1):
                res.append([1])
            elif(i==2):
                res.append([1,1])
            else:
                l1.append(1)
                for j in range(len(res[i-2])-1):
                    l1.append(res[i-2][j]+res[i-2][j+1])
                l1.append(1)
                res.append(l1)
                l1=[]
        return(res)
                    
        
                
            
            
        