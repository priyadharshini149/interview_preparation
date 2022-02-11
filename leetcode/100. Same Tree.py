# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        def sam(root1,root2):
            if(root1==None and root2==None):
                return True
            if(root1!=None and root2!=None):
                return (root1.val==root2.val) and sam(root1.left,root2.left) and sam(root1.right,root2.right)
        return sam(p,q)
        