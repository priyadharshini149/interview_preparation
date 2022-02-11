"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        def pre(root,res):
            if(root==None):
                return None
            if root:
                res.append(root.val)
                for child in root.children:
                    pre(child,res)
            return res
        res=[]
        return pre(root,res)
    
        