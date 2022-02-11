class Solution:
    def findMinArrowShots(self, points):
       
        points=sorted(points,key=lambda x:x[1])
        print(points)
        if(len(points)==0):
            return 0
        end=points[0][1]
        arrow=1
        for i in range(1,len(points)):
            if(points[i][0]>end):
                arrow+=1
                end=points[i][1]
        return arrow
            