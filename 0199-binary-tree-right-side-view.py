# https://leetcode.com/problems/binary-tree-right-side-view/submissions/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    res = []
    
    def rightSideView(self, root: Optional[TreeNode], idx = 0) -> List[int]:
        def helper(root,idx):
            if not root: return []

            if idx == len(self.res): self.res.append(root.val)

            helper(root.right,idx+1)
            helper(root.left,idx+1)

            return self.res
        
        self.res = []
        return helper(root,0)
    