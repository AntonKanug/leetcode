# https://leetcode.com/problems/distribute-coins-in-binary-tree/submissions/
# medium - graph

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    moves = 0

    def distributeCoins(self, root: TreeNode) -> int:
        
        def helper(node):
            if not node: return 0
            
            left = helper(node.left)
            right = helper(node.right)
            self.moves += abs(left) + abs(right)
            
            # -1 for it self
            return node.val + left + right - 1
            
        helper(root)
        
        return self.moves