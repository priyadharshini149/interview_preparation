class Solution(object):
    def partition(self, s):
        if not s: return [[]]
        ans = []
        for i in range(1, len(s) + 1):
            print(s[:i])
            if s[:i] == s[:i][::-1]:  # prefix is a palindrome
                
                for suf in self.partition(s[i:]):
                  
                    ans.append([s[:i]] + suf)
        return ans
        