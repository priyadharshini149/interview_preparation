class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        prev=-1
        m=-1
        
        for i in range(len(seats)):
            if seats[i] == 1:
                if prev == -1:
                    m=i
                else:
                    m=max(m,(i-prev)//2)
                prev =i
        return max(m,len(seats)-1-prev)
        