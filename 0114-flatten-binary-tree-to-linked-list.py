# https://leetcode.com/problems/flatten-binary-tree-to-linked-list/submissions/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    prev = None
    
    def flatten(self, root: TreeNode) -> None:
        if not root: return None
        
        # sol 1
        self.flatten(root.right)
        self.flatten(root.left)

        root.right = self.prev
        root.left = None
        self.prev = root

        # sol 2
        
#         order = []

#         def dfs(node):
#             if not node: return
#             order.append(node)
#             dfs(node.left)
#             dfs(node.right)
            
#         dfs(root)
        
#         for i in range(len(order)-1):
#             order[i].left = None
#             order[i].right = order[i+1]
            