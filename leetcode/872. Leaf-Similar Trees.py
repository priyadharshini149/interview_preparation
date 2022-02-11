# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        def leaf(root1,l):
            if root1:
                if root1.left is None and root1.right is None:
                    l.append(root1.val)
                leaf(root1.left,l)
                leaf(root1.right,l)
        l1=[]
        l2=[]
        leaf(root1,l1)
        leaf(root2,l2)
        return l1==l2