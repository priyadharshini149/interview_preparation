# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        def search(root,data):
            if(root==None):
                return None
            if(root.val==data):
                return root
            if(root.val<data):
                return search(root.right,data)
            if(root.val>data):
                return search(root.left,data)
        return search(root,val)
            
                