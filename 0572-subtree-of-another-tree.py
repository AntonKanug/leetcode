# https://leetcode.com/problems/subtree-of-another-tree/submissions/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    x = None
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode], checkTree = False) -> bool:
        if not self.x: self.x = subRoot

        if not root and not subRoot: return True
        
        if root and subRoot:
            if root.val == subRoot.val:
                if self.isSubtree(root.left, subRoot.left, True) and self.isSubtree(root.right, subRoot.right, True):
                    return True
    
            if not checkTree:
                return self.isSubtree(root.left, self.x, False) or self.isSubtree(root.right, self.x, False) 
        
        return False
        