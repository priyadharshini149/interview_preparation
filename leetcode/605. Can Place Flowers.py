class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        flowerbed = [0]+flowerbed +[0]
        
        for i in range(1,len(flowerbed)-1):
            
            if(flowerbed[i] or flowerbed[i-1] or flowerbed[i+1]):
                continue
            
            else:
                flowerbed[i]=1
                n-=1
        
        return(n<=0)
                    
        
      
        