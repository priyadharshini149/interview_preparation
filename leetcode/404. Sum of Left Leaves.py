# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.sum=0
        def sumofleft(root):
            if(root==None):
                return 
            if(root.left!=None and root.left.left==None and root.left.right==None):
                self.sum+=root.left.val
            sumofleft(root.left)
            sumofleft(root.right)
        sumofleft(root)
        return self.sum
                
        