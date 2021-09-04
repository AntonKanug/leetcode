# https://leetcode.com/problems/maximum-average-subtree/submissions/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    maxV = float('-inf')
    
    def maximumAverageSubtree(self, root: Optional[TreeNode]) -> float:
        
        # returns -> [count, numOfNodes]
        def helper(root):
            if not root: return [0, 0]
            
            l, r = helper(root.left), helper(root.right)
            
            toReturn = [l[0] + r[0] + root.val, l[1] + r[1] + 1]
                        
            self.maxV = max(self.maxV, toReturn[0]/toReturn[1])
            
            return toReturn
            
        helper(root)
        
        return self.maxV