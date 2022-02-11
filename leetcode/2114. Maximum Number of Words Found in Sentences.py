class Solution(object):
    def mostWordsFound(self, sentences):
        """
        :type sentences: List[str]
        :rtype: int
        """
        lenmax=0
        for i in sentences:
            lenmax=max(lenmax,len(i.split(" ")))
        return lenmax
            
        