# https://leetcode.com/problems/diameter-of-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxdiam = 0
        
        def helper(root):
            if not root: return 0
            l, r = helper(root.left), helper(root.right)
            
            nonlocal maxdiam
            maxdiam = max(maxdiam, l + r)
            
            return 1 + max(l, r)
        
        helper(root)
        return maxdiam
    