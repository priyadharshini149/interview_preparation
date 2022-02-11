class WordDictionary(object):

    def __init__(self):
        self.dic={}
        

    def addWord(self, word):
        """
        :type word: str
        :rtype: None
        """
        
        l=len(word)
        if l not in self.dic:
            self.dic[l]=[word]
        else:
             if word not in self.dic[l]:
                    self.dic[l].append(word)
        
       
        

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if len(word) in self.dic:
            s=self.dic[len(word)]
            if word in s:
                return True
            else:
                flag=0
                for i in s:
                    c=0
                    for j in range(len(word)):
                        if(i[j]==word[j]):
                            c+=1
                        elif(word[j]=='.'):
                            c+=1
                    if(c==len(word)):
                        flag=1
                return flag==1
                
                    
                
            
            
        
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)