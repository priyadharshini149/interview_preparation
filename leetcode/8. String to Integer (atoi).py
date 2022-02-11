class Solution:
    def myAtoi(self, s):
        s = s.strip()
        neg = 0
        numbers = ""
        for i, c in enumerate(s):
            if i == 0:
                if c == "+":
                    continue
                if c == "-":
                    neg = 1
                    continue
            
            if c.isdigit():
                numbers += c
                
            elif not c.isdigit():
                break
        
        number = 0 if not numbers else int(numbers)
        if neg == 1:
            return max(-2**31, -number)
        return min(2**31 - 1, number)