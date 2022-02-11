class Solution(object):
    def sequentialDigits(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: List[int]
        """
        res=[1,2,3,4,5,6,7,8,9]
        r=[]
        for i in range(len(res)):
            for j in range(i+1,len(res)):
                s="".join(map(str,res[i:j+1]))
                # print(s)
                if(int(s)>=low and int(s)<=high):
                    r.append(int(s))
        r.sort()
        return(r)

                
            