# https://leetcode.com/problems/count-good-nodes-in-binary-tree/submissions/
# medium

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    count = 0

    def goodNodes(self, root: TreeNode) -> int:        
        
        def helper(root, maxNum):
            if not root: return
            
            maxTemp = maxNum
            
            if root.val >= maxNum:
                self.count+=1
                maxTemp = root.val
            
            helper(root.left, maxTemp)
            helper(root.right, maxTemp)
        
        helper(root,float('-inf'))

        return self.count
                
            