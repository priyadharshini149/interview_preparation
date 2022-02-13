class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        s=set(wordList)
        dq=deque()
        dq.append((beginWord,0))
        while dq:
            w,d=dq.popleft()
            if(w==endWord):
                return d+1
            w=list(w)
            for i in range(len(w)):
                t=w[i]
                for j in range(ord('a'),ord('z')+1):
                    if(t==chr(j)):
                        continue
                    w[i]=chr(j)
                    new="".join(w)
                    if new in s:
                        s.remove(new)
                        dq.append((new,d+1))
                w[i]=t
        return 0
                      