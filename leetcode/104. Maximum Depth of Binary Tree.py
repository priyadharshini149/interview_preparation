# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.result=0
        def maxd(root,depth):
            
            if not root:
                self.result=max(depth,self.result)
                return
            depth+=1
            maxd(root.left,depth)
            maxd(root.right,depth)
                
        maxd(root,0)
        return self.result
        