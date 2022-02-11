class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        # ma=-1
        # for i in range(len(heights)):
        #     mi=float("inf")
        #     for j in range(i,len(heights)):
        #         mi=min(mi,heights[j]);
        #         ma=max(ma,mi*(j-i+1))
        # return(ma)
        
        stack=[]
        left=[]
        right=[]
        
        for i in range(len(heights)):
            if(len(stack)==0):
                left.append(0)
                stack.append(i)
            else:
                while(len(stack)!=0 and heights[stack[-1]]>=heights[i]):
                    stack.pop()
                
                el= 0 if len(stack)==0 else stack[-1]+1
                left.append(el) 
                stack.append(i)
        stack=[]
        for i in range(len(heights)-1,-1,-1):
            if(len(stack)==0):
                right.append(len(heights)-1)
                stack.append(i)
            else:
                while(len(stack)!=0 and heights[stack[-1]]>=heights[i]):
                    stack.pop()
                
                el= len(heights)-1 if len(stack)==0 else stack[-1]-1
                right.append(el) 
                stack.append(i)
        right[:]=right[::-1]
#         print(left)
        
#         print(right)
        m=0
        for i in range(len(heights)):
            # print((right[i]-left[i]+1)*heights[i])
            m=max(m,((right[i]-left[i]+1)*heights[i]))
            # print(m)
        return(m)
            