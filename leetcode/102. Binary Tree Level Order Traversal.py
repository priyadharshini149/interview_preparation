# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        s=[]
        queue=[root]
        
        while(queue):
            s.append([node.val for node in queue])
            l=[]
            for node in queue:
                if(node.left):
                     l.append(node.left)
                if(node.right):
                     l.append(node.right)
            queue=l
        return s
        