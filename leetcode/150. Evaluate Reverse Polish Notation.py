class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for i in range(len(tokens)):
            if(tokens[i]=='+' or tokens[i]=='*' or tokens[i]=='-' or tokens[i]=='/'):
                el=int(stack.pop())
                el2=int(stack.pop())
                if(tokens[i]=='*'):
                    stack.append(el*el2)
                if(tokens[i]=='+'):
                    stack.append(el+el2)
                if(tokens[i]=='-'):
                    stack.append(el2-el)
                if(tokens[i]=='/'):
                    stack.append(int(el2/el))
            else:
                stack.append(int(tokens[i]))
            
        return stack[0]