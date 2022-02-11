
class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        res=[]
        a=dict(Counter(words))
        
        a=sorted(a.items(),key=lambda x:(-x[1],x[0]))
        print(a)
        for i in range(k):
            
            res.append(a[i][0])
        return(res)
        