class Solution:
    def reverseWords(self, s):
        l=list(s.split(" "))
        for i in range(len(l)):
            l[i]="".join(reversed(l[i]))
        
        return(" ".join(l))
        