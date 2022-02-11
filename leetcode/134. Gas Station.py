class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        
        
#         for i in range(len(gas)):
#             st=i
#             curgas=gas[st]-cost[st]
#             st=(st+1)%len(gas)
#             while(i!=st):
#                 if(curgas<0):
#                     break
#                 curgas+=(gas[st]-cost[st])
#                 st=(st+1)%len(gas)
                
#             if(curgas>=0):
#                 return i
#         return -1
          
        if(sum(gas)<sum(cost)):
            return -1
        temp=0
        start=0
        for i in range(len(gas)):
            temp+=gas[i]-cost[i]
            if(temp<0):
                temp=0
                start=i+1
        return start


    
