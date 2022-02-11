class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        def dfs(image,sr,sc,newColor,row,column,source):
            if(sr<0 or sr>=row or sc<0 or sc>=column):
                return
            elif(image[sr][sc]!=source):
                return
            image[sr][sc]=newColor
            
            #top
            dfs(image,sr-1,sc,newColor,row,column,source)
            #down
            dfs(image,sr+1,sc,newColor,row,column,source)
            #left
            dfs(image,sr,sc-1,newColor,row,column,source)
            #right
            dfs(image,sr,sc+1,newColor,row,column,source)
        
        
        if(newColor==image[sr][sc]):
            return image
        row=len(image)
        col=len(image[0])
        source=image[sr][sc]
        dfs(image,sr,sc,newColor,row,col,source)
        return image
        