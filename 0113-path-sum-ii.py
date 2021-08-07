# https://leetcode.com/problems/path-sum-ii/submissions/
# O(n) - Time
# O(lgn) - Space (recursion depth)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        output = []
        
        def helper(root, res, resSum, target):
            if not root: return
            if resSum + root.val == target and not root.left and not root.right: 
                output.append(res + [root.val])
                return
            
            helper(root.left, res + [root.val], resSum + root.val, target)
            helper(root.right, res + [root.val], resSum + root.val, target)
            
        helper(root, [], 0, targetSum)
        return output
    