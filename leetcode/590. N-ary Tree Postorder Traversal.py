"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        def post(root,res):
            if(root==None):
                return None
            if root:
                for child in root.children:
                    post(child,res)
                res.append(root.val)
            return res
        
        res=[]
        return post(root,res)
        
        
        
    