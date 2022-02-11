# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res=[]
        self._post(root,res)
        return res
    def _post(self,root,res):
        if root is not None:
            self._post(root.left,res)
            self._post(root.right,res)
            res.append(root.val)
        