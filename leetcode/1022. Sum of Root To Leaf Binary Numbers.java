/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    int ans;
     void dfs(TreeNode node,int far)
    {
        far=far*2+node.val;
        if(node.left==null && node.right==null)
        {
            ans+=far;
        }
        if(node.left!=null)
        {
            dfs(node.left,far);
        }
           if(node.right!=null)
        {
            dfs(node.right,far);
        }
    }
    public int sumRootToLeaf(TreeNode root)
    {
        dfs(root,0);
        return(ans);
        
    }
}