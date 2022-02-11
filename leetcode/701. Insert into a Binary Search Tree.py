# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
     def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
            if root == None:
                return TreeNode(val)

            def CreateTree(node,value):
                if node == None:
                    return TreeNode(value)
                elif value<node.val:
                    node.left = CreateTree(node.left,value)
        
                elif value>node.val:
                     node.right = CreateTree(node.right,value)
        
                return node
    
            CreateTree(root,val)
            return root